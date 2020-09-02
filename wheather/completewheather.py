import requests
from tkinter import *
import pandas as pd

p = 1
df = pd.DataFrame(columns=['CITY/STATE', 'WEATHER', 'HUMIDITY', 'TEMPERATURE ', 'WIND_SPEED'])

def weather():
    city = city_name.get()
    apikey = "&APPID=9f1ce1bdafac6e1028a201e8114e3f48"
    url = 'https://api.openweathermap.org/data/2.5/weather?q='
    sum = url + city + apikey
    res = requests.get(sum)
    output = res.json()

    weather_status = output['weather'][0]['description']
    temperature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']

    global p
    df.loc[p] = [city] + [weather_status] + [humidity] + [temperature - 273] + [wind_speed]
    df.to_excel("C:\\Users\\Komal\\Documents\\rohan\\weather.xlsx")
    print(df)
    p += 1

    weather_status_label.configure(text="weather status : " + weather_status)
    temprature_label.configure(text="temprature : " + (str(temperature)+"k"))
    humidity_label.configure(text="Humidity : " + str(humidity))
    wind_speed_label.configure(text="wind speed  : " + str(wind_speed))


window = Tk()
window.geometry("400x300")

city_name = StringVar(window)
option = Entry(window, width=20, textvariable=city_name)
option.grid(row=2, column=2, padx=150, pady=10)

b1 = Button(window, text="click to view", width=15, command=weather)
b1.grid(row=5, column=2, padx=150)

weather_status_label = Label(window, font=("times", 12, "bold italic"))
weather_status_label.grid(row=10, column=2)

temprature_label = Label(window, font=("times", 12, "bold italic"))
temprature_label.grid(row=12, column=2)

humidity_label = Label(window, font=("times", 12, "bold italic"))
humidity_label.grid(row=14, column=2)

wind_speed_label = Label(window, font=("times", 12, "bold italic"))
wind_speed_label.grid(row=16, column=2)

window.mainloop()