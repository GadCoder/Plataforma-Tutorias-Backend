from fastapi import APIRouter, Request, HTTPException
from domain.services.authenticate import get_student_token


api_router = APIRouter()  


@api_router.get("/check_api")
async def check_api():
    return {"status": "Connected to API Successfully"}


@api_router.post("/login-student")
async def auth_student(request: Request):
    body = await request.json()
    username = body.get('username')
    password = body.get('password')
    response = get_student_token(user=username, password=password)
    if response is None:
        raise HTTPException(status_code=401, detail="Unauthorized")   
    return response