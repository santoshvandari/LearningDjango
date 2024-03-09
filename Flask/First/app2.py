import flask

app=flask.Flask(__name__)

@app.route('/')
def Home():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is about page"

if __name__=="__main__":
    # Run the app in 8000 port
    app.run(debug=True,port=8000)
