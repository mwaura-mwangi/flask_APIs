from app import db


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    # Add explicit __init__ for static type checkers
    def __init__(self, title: str, completed: bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

   