from fastapi import APIRouter

router=APIRouter(prefix='/products')

@router.get('/')
async def product():
    return {"message":'products'}

@router.get('/test')
async def test():
    return {"ajbglabgjlhb"}


