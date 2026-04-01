from fastapi import FastAPI
from products.urls import router as product_router



app=FastAPI()


app.include_router(router=product_router)
@app.get('/')
async def test():
    return {'message':'salom dunyo'}

@app.get('/test')
async def test1():
    return {'akjsdfhkabgkab'}