import flask

app=flask.Flask(__name__)

@app.route('/')
def Home():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is about page"

if __name__=="__main__":
    app.run(debug=True)