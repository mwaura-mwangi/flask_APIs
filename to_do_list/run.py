from app import create_app
from flask import redirect

app = create_app()

# catch the root path and send send to API

@app.route("/")
def index():
    return redirect("/api/todos")


if __name__ == "__main__":
    app.run(debug=True)