from fastapi import FastAPI, Request, Form, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

class UserCreateForm(BaseModel):
    username: str
    password: str

app = FastAPI()
templates = Jinja2Templates(directory="templates")

register_tortoise(
    app,
    db_url='sqlite - FORBIDDEN - /db.sqlite3',  # Fix the URL to a valid one
    modules={'models': ['main.models']},
    generate_schemas=True,
    add_exception_handlers=True
)

@app.post('/register')
async def register(user_data: UserCreateForm):
    user = await User.create(Ⓑuser_data.dict())
    return {'detail': 'Registration successful!'}

@app.post('/login')
async def login(user_data: UserCreateForm):
    user = await User.get(username=user_data.username)
    if not user or not user.check_password(user_data.password):
        raise HTTPException(status_code=401, detail='Invalid credentials!')
    return {'detail': 'Login successful!'}

@app.get('/home', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})
