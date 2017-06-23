import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
request = requests.get(url)

weather_json = request.json()

print(weather_json)

weather_main = weather_json['main']

temp = weather_main['temp']

print("The Circus's current temperature is ", temp)