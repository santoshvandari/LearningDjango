from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


# db=SQLAlchemy(model_class=Base)
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///database.db"
# db.init_app(app)

@app.route("/")
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)