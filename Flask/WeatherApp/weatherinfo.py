import requests,socket

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

