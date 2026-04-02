from fastapi import APIRouter

router=APIRouter(prefix='/users')


@router.get("/")
async def get():
    return {"message":"user bo'limi "}


@router.post("/user")
async def post():
    pass

    