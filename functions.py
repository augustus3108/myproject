import requests
import json
import tkinter as tk
import tkinter
import tkinter.messagebox
import customtkinter
import re 
#from decouple import config


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green



OPEN_WEATHER_MAP_API_KEY = '238610ef59bf170fd07ab74c164e5567' 
OPEN_WEATHER_MAP_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather" 

IPBASE_API_KEY = 'hGSjjIxYWg4dF0cdgrqxKcMuB5w1GqsgEmSkNKWJ'
IPBASE_API_ENDPOINT = "https://api.ipbase.com/v2/info"

IP_ADDRESS_REGEX = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
def get_weather():
    input_value = input_field.get() 

    if IP_ADDRESS_REGEX.match(input_value):
        ipbase_query_params = {
            "apiKey" : IPBASE_API_KEY,
            "ip" : input_value
        }
        response = requests.get(IPBASE_API_ENDPOINT, params=ipbase_query_params)
        city_name =  response.json()["data"]["location"]["city"]["name"]

        weather_query_params = {
            'q' : city_name,
            'appid' : OPEN_WEATHER_MAP_API_KEY,
            'units' : 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()

    else:
        weather_query_params = {
            'q' : input_value,
            'appid' : OPEN_WEATHER_MAP_API_KEY,
            'units' : 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()
        print(weather_data)
        out_file = open("WeatherData4.json","w")
        json.dump(weather_data, out_file, indent=6)
        #Display weather data
        weather_label.config(
            text=f"Temperature: {weather_data['main']['temp']}°C")
        
        feels_like_label.config(
        text=f"Feels Like: {weather_data['main']['feels_like']}°C")

        pressure.config(
        text=f"Pressure: {weather_data['main']['pressure']} mb")

        humidity.config(
        text=f"Humidity: {weather_data['main']['humidity']} %")

         

        


    

def get_location_weather():
    query_params = {
        "apiKey" : IPBASE_API_KEY
    }
    response = requests.get(IPBASE_API_ENDPOINT, params=query_params)
    city_name = response.json()["data"]["location"]["city"]["name"]

    weather_query_params = {
        'q' : city_name,
        'appid' : OPEN_WEATHER_MAP_API_KEY,
        'units' : 'metric'
    }
    response = requests.get(
        OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    #Display weather data
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']} C"
    )

    

root = customtkinter.CTk()
root.title("Weather Forecast App")
root.geometry("500x450")



input_field = customtkinter.CTkEntry(root, corner_radius = 20, width=200, height=40, border_width=5, placeholder_text="Enter city or IP address", text_color="yellow")
input_field.pack()


submit_button = customtkinter.CTkButton(root, text="GET WEATHER", command=get_weather, height= 35)
submit_button.pack()

location_button = customtkinter.CTkButton(root, text="USE CURRENT LOCATION", command=get_location_weather, height= 25)
location_button.pack()

weather_label = tk.Label(root, text="",width=20, font="Sans-serif", fg='green')
weather_label.pack()

feels_like_label = tk.Label(root, text="", width=20, font="Sans-serif", fg='green',)
feels_like_label.pack()

pressure = tk.Label(root, text="",width=20,font="Sans-serif", fg='green')
pressure.pack()

humidity = tk.Label(root, text="", width=20, font="Sans-serif",fg='green')
humidity.pack()



root.mainloop()



        