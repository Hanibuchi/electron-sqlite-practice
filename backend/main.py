from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# 起動時にDBとテーブルを準備
def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    conn.close()

init_db()

class Task(BaseModel):
    content: str

@app.post("/add_task")
def add_task(task: Task):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (content) VALUES (?)", (task.content,))
    conn.commit()
    conn.close()
    return {"message": f"Saved: {task.content}"}

@app.get("/get_tasks")
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return {"tasks": [row[0] for row in rows]}