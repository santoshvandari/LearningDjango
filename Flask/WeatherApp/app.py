from flask import Flask,render_template,request
import datetime
from weatherinfo import getWeatherInfo

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    weatherinfo= getWeatherInfo()
    if request.method == 'POST':
        city = request.form['city']
        weatherinfo = getWeatherInfo(city)
    # Converting the Unix Time Format to Standard Time Format 
    sunrise_datetime = datetime.datetime.utcfromtimestamp(weatherinfo["data"]["sunrise"])
    sunset_datetime = datetime.datetime.utcfromtimestamp(weatherinfo["data"]["sunset"])
    weatherinfo["data"]["sunrise"] = sunrise_datetime.strftime("%I:%M %p")
    weatherinfo["data"]["sunset"] = sunset_datetime.strftime("%I:%M %p")
    return render_template('index.html',weatherinfo=weatherinfo)