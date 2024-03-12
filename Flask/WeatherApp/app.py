from flask import Flask,render_template,request
import requests,socket,datetime

app = Flask(__name__)

def getWeatherInfo(city="Kathmandu"):
    url = 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city='+city
    try:
        socket.create_connection(("1.1.1.1", 53))
        response = (requests.get(url, headers={ 'X-RapidAPI-Key': '1455199545msh53bfce68da0845bp10119cjsn23566562dee1'}))
        if response.status_code == requests.codes.ok:
            # add the status code in response
            response= {"status_code": response.status_code,"city" : city, "data": response.json()}
            weatherinfo = response
        else:
            weatherinfo= {"status_code": response.status_code, "Error": response.text}
        return weatherinfo
    except Exception as exep:
        weatherinfo= {"status_code": 101, "error": "Network is Unreachable"}
        return weatherinfo

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

if __name__ == '__main__':
    app.run(debug=True)
    pass