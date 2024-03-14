from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app=Flask(__name__)

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(1000), nullable=False)
    def __repr__(self):
        return f"Todo {self.id}"

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title=(request.form['title']).strip()
        desc=(request.form['desc']).strip()
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    todos=Todo.query.all()
    return render_template('index.html',todos=todos)

@app.route('/delete/<int:id>')
def delete(id):
    todo=Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    todo=Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.title=(request.form['title']).strip()
        todo.desc=(request.form['desc']).strip()
        db.session.commit()
        return redirect('/')
    return render_template('update.html',todo=todo)


if __name__ == '__main__':
    app.run(debug=True)