from fastapi import APIRouter, HTTPException, status, Depends
from .auth import auth_user

from db.client import products
from db.models.model_item import ProductsResponse, ProductsForm

router = APIRouter(prefix='/products', tags=['Products'])

def shearProduct(key, value):
    product = products.find_one({key: value})

    if product:
        product['_id'] = str(product['_id'])
        del product['_id']
        return ProductsResponse(**product)
    else:
        return None


@router.post('/create', status_code=201)
async def create(data: ProductsForm, token = Depends(auth_user)):
    if shearProduct(key='name', value=data.name):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='existing product'
        )
    
    product = data.dict()
    products.insert_one(product).inserted_id

    return 'Producto añadido'

@router.get('/get', status_code=200)
async def get_products(token = Depends(auth_user)):
    products_list = []
    for p in products.find():
        p['_id'] = str(p['_id'])
        del p['_id']
        products_list.append(p)

    return products_list

@router.get('/alert', status_code=200)
async def get_product(token = Depends(auth_user)):
    products_list = []
    for p in products.find():
        p['_id'] = str(p['_id'])
        del p['_id']
        if p['stock'] < 10:
            products_list.append(p)

    return products_list

@router.get('/get/{name}', status_code=200)
async def alert(name:str, token = Depends(auth_user)):
    product = products.find_one({'name': name})

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el producto'
        )
    
    product['_id'] = str(product['_id'])
    del product['_id']

    return product


@router.delete('/delete/{name}', status_code=200)
async def delete(name:str, token = Depends(auth_user)):
    product = products.delete_one({'name': name})

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el producto'
        )
    

    return {'msg': 'Producto eliminado'}