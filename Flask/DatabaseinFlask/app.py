from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"
db=SQLAlchemy(app)

class StudentInfo(db.Model):
    rollno=db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(50),nullable=False)
    Address=db.Column(db.String(70),nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.rollno},{self.fullname},{self.Address}"
    
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)