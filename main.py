import requests as rq
import json
import os

if __name__ == '__main__':

    print("Welcome to weather app by Sanjeev")
    cityName = input("Enter your city name :\n ")

    api ="YOUR API KEY HERE" #Put your API key here

        #you can get your own API key from https://www.weatherapi.com/
    url = f"https://api.weatherapi.com/v1/current.json?key={api}&q={cityName}"
    get = rq.get(url)

    jsonData = json.loads(get.text)
    current_condition = jsonData["current"]["condition"]["text"]
    current_temp = jsonData["current"]["temp_c"]
    feelslike_c = jsonData["current"]["feelslike_c"]
    wind_kph = jsonData["current"]["wind_kph"]
    humidity = jsonData["current"]["humidity"]
    vis_km = jsonData["current"]["vis_km"]
    gust_kph = jsonData["current"]["gust_kph"]

    os.system(f"say It is '{current_condition} and {current_temp} degree in {cityName}'")

    while True:
        requestedInput = input('''More Options : 
           1. Feels Like
           2. Wind Speed(kmh)
           3. Humidity 
           4. Visibility in Km
           5. Gust in Km
           6. Exit\n
           Enter your choice : ''')
        reqSt = int(requestedInput)
        match reqSt:
            case 1:
                os.system(f"say It feels like '{feelslike_c} degree in {cityName}'")
            case 2:
                os.system(f"say Wind speed is '{wind_kph} kilometer per hour in {cityName}'")
            case 3:
                os.system(f"say Humidity is '{humidity} in {cityName}'")
            case 4:
                os.system(f"say Visibility is '{vis_km} kilometer per hour in {cityName}'")
            case 5:
                os.system(f"say Gust is '{gust_kph}  kilometer per hour din {cityName}'")
            case 6:
                os.system(f"say See you soon.")
                break
