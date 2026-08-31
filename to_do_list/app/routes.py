from flask import Blueprint, request, jsonify
from app import db
from app.models import Todo
from flask import redirect


todo_bp = Blueprint("todos", __name__, url_prefix="/api/todos")


@todo_bp.route("/info", methods=["GET"])
def index_info():
    return jsonify({
        "status": "online",
        "message": "Todo API is running",
        "endpoints": "/api/todos/"
    })


@todo_bp.route("/redirect", methods=["GET"])
def index_redirect():
    return redirect("/api/todos/")


# GET /api/todos
@todo_bp.route("/", methods=["GET"])
def get_todos():
    todos = Todo.query.all()

    return jsonify([
        todo.to_dict()
        for todo in todos
    ])


# GET /api/todos/<id>
@todo_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = db.get_or_404(
        Todo, todo_id, description="Todo not found"
        )

    return jsonify(todo.to_dict())


# POST /api/todos
@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400

    todo = Todo(
        title=data["title"],
        completed=data.get("completed", False)
    )

    db.session.add(todo)
    db.session.commit()

    return jsonify(todo.to_dict()), 201


# PUT /api/todos/<id>
@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = db.get_or_404(
        Todo, todo_id, description="Todo not found"
        )

    data = request.get_json()

    if "title" in data:
        todo.title = data["title"]

    if "completed" in data:
        todo.completed = data["completed"]

    db.session.commit()

    return jsonify(todo.to_dict())


# DELETE /api/todos/<id>
@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = db.get_or_404(
        Todo, todo_id, description="Todo not found"
        )

    db.session.delete(todo)
    db.session.commit()

    return jsonify({
        "message": "Todo deleted successfully"
    })