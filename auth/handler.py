from fastapi import APIRouter

auth = APIRouter()

auth.post('/register')
def register():
