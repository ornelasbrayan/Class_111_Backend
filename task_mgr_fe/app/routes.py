from flask import (
    Flask, 
    render_template,
    request
)
from datetime import datetime
import requests

BACKEND_URL = "http://127.0.0.1:5000"
app = Flask(__name__)

@app.get("/")
def index():
    timestamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("index.html", server_time=timestamp)

@app.get("/tasks")
def show_tasks():
    url = "%s/tasks" % BACKEND_URL
    resp = requests.get(url)
    if resp.status_code == 200:
        task_list = resp.json().get("tasks")
        return render_template("task_list.html", tasks=task_list)
    return render_template("error.html"), resp.status_code

@app.get("/tasks/<int:pk>")
def task_detail(pk):
    url = "%s/tasks/%s" % (BACKEND_URL, pk)
    resp = requests.get(url)
    if resp.status_code == 200:
        task = resp.json().get("task")
        return render_template("task_detail.html", task=task)
    return render_template("error.html"), resp.status_code

@app.get("/tasks/new")
def new_task_form():
    return render_template("new.html")

@app.post("/tasks/new")
def create_task():
    task_data = {
        "summary": request.form.get("summary"),
        "description": request.form.get("description"),
        "status_id": request.form.get("status_id"),
        "active": request.form.get("active")
    }
    url = '%s/tasks' % BACKEND_URL
    resp = requests.post(url, json=task_data)
    if resp.status_code == 204:
        return render_template("success.html")
    return render_template("error.html"), resp.status_code
    