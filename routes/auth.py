from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt
import os

from db.models.model_user import UserDB, UserForm, UserResponse
from db.client import users

load_dotenv()

router = APIRouter(prefix='/auth', tags=['auth'])

crypt = CryptContext(schemes=['argon2'])
oauth = OAuth2PasswordBearer('/auth/login')
SECRET = os.getenv('SECRECT_KEY')

def shearUser(key, value):
    user = users.find_one({key: value})

    if not user:
        return None
        
    user['_id'] = str(user['_id'])
    return UserDB(**user)

def auth_user(token = Depends(oauth)):
    data = jwt.decode(token, key=SECRET)


@router.post('/register', status_code=201)
async def register(data: UserForm):

    if shearUser('email', data.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="email ya registrado"
        )

    hashed_password = crypt.hash(data.password)

    user_doc = data.dict()
    user_doc['password'] = hashed_password

    users.insert_one(user_doc)

    return {"message": "Usuario creado correctamente"}

@router.post('/login', status_code=200)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    
    if not shearUser('email', form.username):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User no existe'
        )
    
    user = shearUser('email', form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='COntraseña incorrecta'
        )
    
    token = jwt.encode({
        'sub': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, SECRET, algorithm='HS256')

    return {
        'acces_token': token,
        'token_type': 'bearer'
    }
