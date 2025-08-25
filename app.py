from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# 🏠 الصفحة الرئيسية
@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# ➕ إضافة مهمة
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# 🗑️ حذف مهمة
@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

# ✏️ تعديل مهمة
@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    if task:
        new_title = request.form.get('title')
        if new_title:
            task.title = new_title
            db.session.commit()
    return redirect(url_for('index'))

# ✅ تغيير حالة المهمة (منجزة أو لا)
@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
