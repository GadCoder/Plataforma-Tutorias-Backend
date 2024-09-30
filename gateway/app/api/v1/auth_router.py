import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from schemas.user import UserCredentials


load_dotenv()

AUTH_BASE_URL = os.environ.get("AUTH_BASE_URL")

router = APIRouter()

@router.post("/login_student")
async def login_student(credentials: UserCredentials):
    try:
        print(f"{AUTH_BASE_URL}/api/v1/auth/login-student/")
        response = requests.post(f"{AUTH_BASE_URL}/api/v1/auth/login-student/", json={"username": credentials.username, "password": credentials.password})
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.json())
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Authentication service is unavailable")