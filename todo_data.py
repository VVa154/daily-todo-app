# todo_data.py
"""
Handles storage and operations for the Daily To-Do app
"""

from datetime import datetime

#Dictionary to store todos
#Key=date, Value=list of tasks

todo_data={}

def get_today_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_todos(date=None):
    if date is None:
        date=get_today_date()
    return todo_data.get(date,[])

def add_todo(task, date=None):
    if date is None:
        date= get_today_date()
    if date not in todo_data:
        todo_data[date]=[]
    todo_data[date].append({"task":task,"done":False})

def mark_done(index, date=None):
    if date is None:
        date = get_today_date()
    if date in todo_data and 0 <= index < len(todo_data[date]):
        todo_data[date][index]["done"] = True

