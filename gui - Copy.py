import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600
root = tk.Tk()

def format(weather):
    try:
        name = (weather['name'])
        description =(weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        final_str = "City: %s \n Conditions: %s \n Temperature in Farenheit: %s \n" % (name, description, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str
def get_weather(city):
    weather_key= 'ffaadbd389aae5ad8152c3a481a5afef'
    url ='https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url,params = params)
    weather =response.json()
    label['text'] = format(weather)

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
def func(entry):
    print("This is the entry:", )

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='sam.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1, anchor = 'n')

frame = tk.Frame(root, bg='#80c1ff', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=.75, relheight= 0.1, anchor = 'n',)

entry = tk.Entry(frame, font=('Courier', 17))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text ="Get weather", fg ='green', font = ('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd= 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight= 0.6, anchor ='n')

label = tk.Label(lower_frame, font = ('Bold', 20))
label.place(relwidth=1, relheight=1)



root.mainloop()