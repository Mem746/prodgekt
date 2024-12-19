from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/tasks", response_class=HTMLResponse)
async def tasks(request: Request):
    tasks = ["Task 1", "Task 2", "Task 3"]
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})
@app.post("/tasks", response_class=HTMLResponse)
async def create_task(request: Request, task: str = Form(...)):
    tasks = ["Task 1", "Task 2", "Task 3"]
    tasks.append(task)
    return templates.TemplateResponse("tasks.html", {"request": request, "tasks": tasks})