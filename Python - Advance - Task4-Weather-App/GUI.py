import os
import warnings
import urllib3

# Suppress warnings
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)
os.environ['TK_SILENCE_DEPRECATION'] = '1'
warnings.filterwarnings('ignore')

import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather Application")
        self.root.geometry("1000x800")
        self.root.config(bg="#ecf0f1")
        
        self.API_KEY = os.getenv("OPENWEATHER_API_KEY")
        self.current_unit = "metric"
        self.weather_icon_image = None
        self.search_in_progress = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#2c3e50", height=80)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="🌤️ Weather Application", 
                        font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        title.pack(pady=20)
        
        # Control Panel
        ctrl = tk.Frame(self.root, bg="#ecf0f1")
        ctrl.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(ctrl, text="City:", font=("Arial", 12), bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.city_entry = tk.Entry(ctrl, font=("Arial", 12), width=30)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "Phnom Penh")
        
        self.search_btn = tk.Button(ctrl, text="🔍 Search", command=self.on_search_click, 
                 font=("Arial", 11), bg="#3498db", fg="white", padx=15)
        self.search_btn.pack(side=tk.LEFT, padx=5)
        
        tk.Label(ctrl, text="Unit:", font=("Arial", 12), bg="#ecf0f1").pack(side=tk.LEFT, padx=15)
        self.unit_btn = tk.Button(ctrl, text="°C", command=self.toggle_unit, 
                                 font=("Arial", 11), bg="#9b59b6", fg="white", width=5)
        self.unit_btn.pack(side=tk.LEFT, padx=5)
        
        self.city_entry.bind("<Return>", self.on_enter_key)
        
        # Current Weather
        weather_frame = tk.LabelFrame(self.root, text="📍 Current Weather", 
                                     font=("Arial", 13, "bold"), bg="white", bd=2)
        weather_frame.pack(padx=20, pady=10, fill=tk.BOTH)
        
        inner = tk.Frame(weather_frame, bg="white")
        inner.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.icon_label = tk.Label(inner, text="🌤️", font=("Arial", 70), bg="white")
        self.icon_label.pack(side=tk.LEFT, padx=20)
        
        self.weather_text = tk.Label(inner, text="Click Search to load weather", 
                                    font=("Arial", 12), bg="white", justify=tk.LEFT)
        self.weather_text.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
        
        # Hourly Forecast
        hourly_frame = tk.LabelFrame(self.root, text="⏰ Hourly Forecast", 
                                    font=("Arial", 12, "bold"), bg="white", bd=2)
        hourly_frame.pack(padx=20, pady=10, fill=tk.X)
        
        self.hourly_canvas = tk.Canvas(hourly_frame, bg="white", height=100, highlightthickness=0)
        self.hourly_canvas.pack(padx=10, pady=10, fill=tk.X)
        
        # Daily Forecast
        daily_frame = tk.LabelFrame(self.root, text="📅 5-Day Forecast", 
                                   font=("Arial", 12, "bold"), bg="white", bd=2)
        daily_frame.pack(padx=20, pady=10, fill=tk.X)
        
        self.daily_canvas = tk.Canvas(daily_frame, bg="white", height=100, highlightthickness=0)
        self.daily_canvas.pack(padx=10, pady=10, fill=tk.X)
        
        # Status Bar
        self.status = tk.Label(self.root, text="Ready ✓", font=("Arial", 10), 
                              bg="#bdc3c7", fg="black", relief=tk.SUNKEN)
        self.status.pack(fill=tk.X, side=tk.BOTTOM)
    
    def on_enter_key(self, event):
        if not self.search_in_progress:
            self.on_search_click()
    
    def on_search_click(self):
        if self.search_in_progress:
            return
        self.search_in_progress = True
        self.search_btn.config(state=tk.DISABLED)
        self.search_weather()
        self.search_btn.config(state=tk.NORMAL)
        self.search_in_progress = False
    
    def toggle_unit(self):
        self.current_unit = "imperial" if self.current_unit == "metric" else "metric"
        self.unit_btn.config(text="°F" if self.current_unit == "imperial" else "°C")
        if self.city_entry.get().strip() and not self.search_in_progress:
            self.on_search_click()
    
    def display_hourly(self, city):
        try:
            r = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                           params={"q": city, "appid": self.API_KEY, "units": self.current_unit},
                           timeout=5)
            if r.status_code == 200:
                data = r.json()
                self.hourly_canvas.delete("all")
                unit = "°F" if self.current_unit == "imperial" else "°C"
                x = 20
                for i in range(min(6, len(data["list"]))):
                    f = data["list"][i]
                    time = f["dt_txt"].split(" ")[1][:5]
                    temp = int(f["main"]["temp"])
                    cond = f["weather"][0]["main"]
                    text = f"{time}\n{temp}{unit}\n{cond}"
                    self.hourly_canvas.create_text(x, 50, text=text, font=("Arial", 9), fill="#2c3e50")
                    x += 155
        except Exception as e:
            print(f"Hourly error: {e}")
    
    def display_daily(self, city):
        try:
            r = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                           params={"q": city, "appid": self.API_KEY, "units": self.current_unit},
                           timeout=5)
            if r.status_code == 200:
                data = r.json()
                self.daily_canvas.delete("all")
                unit = "°F" if self.current_unit == "imperial" else "°C"
                forecasts = [data["list"][i] for i in range(0, min(40, len(data["list"])), 8)][:5]
                x = 20
                for f in forecasts:
                    date = f["dt_txt"].split(" ")[0]
                    tmax = int(f["main"]["temp_max"])
                    tmin = int(f["main"]["temp_min"])
                    cond = f["weather"][0]["main"]
                    text = f"{date}\nH:{tmax}{unit}\nL:{tmin}{unit}\n{cond}"
                    self.daily_canvas.create_text(x, 50, text=text, font=("Arial", 9), fill="#2c3e50")
                    x += 190
        except Exception as e:
            print(f"Daily error: {e}")
    
    def search_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            self.status.config(text="⚠️ Enter city name", bg="#e74c3c", fg="white")
            return
        
        self.status.config(text="🔄 Loading...", bg="#3498db", fg="white")
        self.root.update()
        
        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": self.API_KEY, "units": self.current_unit}
            
            r = requests.get(url, params=params, timeout=5)
            
            if r.status_code == 200:
                data = r.json()
                
                temp = round(data["main"]["temp"], 1)
                cond = data["weather"][0]["description"].capitalize()
                humid = data["main"]["humidity"]
                wind = round(data["wind"]["speed"], 1)
                press = data["main"]["pressure"]
                feels = round(data["main"]["feels_like"], 1)
                
                unit_sym = "°F" if self.current_unit == "imperial" else "°C"
                wind_unit = "mph" if self.current_unit == "imperial" else "m/s"
                
                # Update icon
                icon_map = {"01d": "☀️", "01n": "🌙", "02d": "⛅", "02n": "☁️", 
                           "03d": "☁️", "04d": "☁️", "09d": "🌧️", "10d": "🌧️",
                           "11d": "⛈️", "13d": "❄️", "50d": "🌫️"}
                icon = icon_map.get(data["weather"][0]["icon"], "🌤️")
                self.icon_label.config(text=icon)
                
                info = f"""City: {city}

Temperature: {temp}{unit_sym}
Feels Like: {feels}{unit_sym}
Condition: {cond}
Humidity: {humid}%
Wind Speed: {wind} {wind_unit}
Pressure: {press} hPa"""
                
                self.weather_text.config(text=info)
                self.display_hourly(city)
                self.display_daily(city)
                self.status.config(text="✅ Weather loaded", bg="#27ae60", fg="white")
                
            elif r.status_code == 404:
                self.status.config(text="❌ City not found", bg="#e74c3c", fg="white")
                self.weather_text.config(text="City not found. Try another city.")
            else:
                self.status.config(text=f"❌ API Error {r.status_code}", bg="#e74c3c", fg="white")
        except requests.exceptions.Timeout:
            self.status.config(text="❌ Connection timeout", bg="#e74c3c", fg="white")
        except requests.exceptions.ConnectionError:
            self.status.config(text="❌ No internet connection", bg="#e74c3c", fg="white")
        except Exception as e:
            self.status.config(text=f"❌ Error: {str(e)}", bg="#e74c3c", fg="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            
            weather_info = f"📍 City: {city}\n\n🌡️ Temperature: {temp}°C\n☁️ Condition: {condition}\n💧 Humidity: {humidity}%"
            weather_text.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch weather: {str(e)}")
        
def display_weather(data):

    location_label.config(
        text=data["name"]
    )

    temperature_label.config(
        text=f'{data["main"]["temp"]}°C'
    )

    description_label.config(
        text=data["weather"][0]["description"].title()
    )

# Button
button = tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#4CAF50", 
                   fg="white", command=get_weather, padx=20, pady=10)
button.pack(pady=10)

location_label = ttk.Label(
    result_frame,
    text="Location"
)

location_label.pack()

temperature_label = ttk.Label(
    result_frame,
    text="--°C"
)

temperature_label.pack()

description_label = ttk.Label(
    result_frame,
    text="Weather"
)

description_label.pack()

humidity_label = ttk.Label(
    result_frame,
    text="Humidity: --%"
)

humidity_label.pack()

humidity_label.config(
    text=f'Humidity: {data["main"]["humidity"]}%'
)

feels_label = ttk.Label(
    result_frame,
    text="Feels like: --°C"
)

feels_label.pack()

feels_label.config(
    text=f'Feels like: {data["main"]["feels_like"]}°C'
)

wind_label = ttk.Label(
    result_frame,
    text="Wind: -- km/h"
)

wind_label.pack()


wind_kmh = data["wind"]["speed"] * 3.6

wind_label.config(
    text=f"Wind: {wind_kmh:.1f} km/h"
)

# icon
icon_code = data["weather"][0]["icon"]
icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

# imgae
image_data = requests.get(icon_url).content
image = Image.open(BytesIO(image_data))
weather_icon = ImageTk.PhotoImage(image)
icon_label.config(image=weather_icon)
icon_label.image = weather_icon
root.mainloop()