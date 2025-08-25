from extensions import db



from extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)  # ✅ العمود الجديد

    def __repr__(self):
        return f'<Task {self.title}>'
