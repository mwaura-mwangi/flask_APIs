from app import create_app, db
from app.models import Todo
from flask import render_template, request, redirect, url_for

app = create_app()

@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")
    if title and title.strip():
        new_todo = Todo(
            title=title.strip(),
            completed=False
        )
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)