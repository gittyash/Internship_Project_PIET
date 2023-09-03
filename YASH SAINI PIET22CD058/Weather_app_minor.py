#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import requests

# API KEY
api_key = 'c6966f15960678a2c31357ee06716639'

# Function to fetch weather data and update GUI
def get_weather():
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        temp_celsius = round(temp - 273.16, 2)
        temperature_label.config(text=f'Temperature: {temp_celsius} °C', fg='blue')

        if temp_celsius < 0:
            weather_label.config(text='☃️ Very Cold', fg='cyan')
        elif 0 <= temp_celsius < 15:
            weather_label.config(text='❄️❄️ Cold', fg='cyan')
        elif 15 <= temp_celsius < 25:
            weather_label.config(text='☁️ Chill', fg='blue')
        elif 25 <= temp_celsius < 35:
            weather_label.config(text='⛅ Sunny', fg='magenta')
        elif 35 <= temp_celsius < 40:
            weather_label.config(text='🥵 Hot', fg='red')
        else:
            weather_label.config(text='🔥 Very Hot', fg='red')

        description_label.config(text=f'Description: {desc}', fg='magenta')
    else:
        messagebox.showerror('Error', 'Error fetching weather data')

# Create GUI
app = tk.Tk()
app.title("Weather App")

city_label = tk.Label(app, text="Enter city name:", fg='black')
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather, bg='green', fg='white')
get_weather_button.pack()

temperature_label = tk.Label(app, text="Temperature: ", fg='blue')
temperature_label.pack()

weather_label = tk.Label(app, text="", fg='cyan')
weather_label.pack()

description_label = tk.Label(app, text="Description: ", fg='magenta')
description_label.pack()

app.mainloop()


# In[ ]:




