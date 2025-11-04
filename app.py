"""
Daily To-Do List app using Flask
"""

from flask import Flask, request, jsonify
from todo_data import get_todos,add_todo,mark_done,get_today_date

app=Flask(__name__)

@app.route("/")
def home():
    return "Daily To-Do List App is running!"


@app.route("/todos", methods=["GET"])
def list_todos():
    date = request.args.get("date")
    todos = get_todos(date)
    return jsonify({"date": date or get_today_date(), "todos": todos})


@app.route("/todos", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    date = data.get("date")
    if not task:
        return jsonify({"error": "Missing task"}), 400
    add_todo(task, date)
    return jsonify({"message": "Todo added"}), 201


@app.route("/todos/<int:index>/done", methods=["POST"])
def complete_task(index):
    date = request.args.get("date")
    mark_done(index, date)
    return jsonify({"message": f"Task {index} marked as done"}), 200

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    app.run(debug=True)


