from fastapi import FastAPI
from config.settings import engine, Base
from products.urls import router as product_router
import users.models
app=FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router=product_router)
@app.get('/')
async def test():
    return {'message':'databasega ulandi '}

@app.get('/test')
async def test1():
    return {'akjsdfhkabgkab'}

