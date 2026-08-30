# 🌤️ Advanced Weather App

**Internship:** Oasis Infobyte (OIBSIP)  
**Track:** Python Development  
**Level:** Advanced Tier  
**Task:** Task 4 – Advanced Weather App

---

## 📌 Project Overview

The **Advanced Weather App** is a high-performance weather application developed as part of the **Oasis Infobyte (OIBSIP) Python Development Internship**.

The application fetches **real-time weather information** from the **OpenWeatherMap API** and presents it through a clean and user-friendly **Graphical User Interface (GUI)** built with Tkinter.

The app focuses on **user experience, security, error handling, and clean software development practices**. Users can search for any city around the world and view its current weather conditions, including temperature, humidity, weather descriptions, and visual weather icons.

---

## ✨ Features

### 🖥️ Interactive GUI

- Built using **Tkinter**
- Simple and intuitive interface
- City input field for weather searches
- Interactive **Get Weather** button
- Dedicated weather results panel
- Dynamically updates weather information

### 🌎 Real-Time Weather Data

- Integrated with the **OpenWeatherMap API**
- Retrieves live weather information
- Supports cities from around the world
- Uses **Metric units (°C)** for temperature

### 🌤️ Visual Weather Elements

- Displays weather icons based on current conditions
- Icons are stored in the `/assets` directory
- Supports visual representations such as:
  - ☀️ Sunny
  - ☁️ Cloudy
  - 🌧️ Rainy
  - ⛈️ Thunderstorm
  - ❄️ Snow
  - 🌫️ Mist/Fog

### 🌡️ Detailed Weather Information

The application displays:

- 🌡️ Temperature
- 💧 Humidity
- 🌤️ Weather description
- 🏙️ City information
- 🖼️ Weather condition icon

### ⚠️ User-Friendly Error Handling

The application handles common API and user input errors without crashing the program.

Examples include:

- `City Not Found`
- Invalid city name
- Missing API key
- Network/API connection errors
- Empty search input

Errors are displayed directly inside the GUI instead of appearing as terminal crashes.

### 🔐 Secure API Key Management

The OpenWeatherMap API key is **never hardcoded** into the Python source code.

Instead, the project uses:

- `.env` for storing the API key
- `python-dotenv` for loading environment variables
- `.gitignore` to prevent `.env` from being uploaded to GitHub

This helps protect the API key from accidental exposure.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.x** | Main programming language |
| **Tkinter** | Graphical User Interface |
| **Requests** | API requests and networking |
| **JSON** | Processing API response data |
| **python-dotenv** | Environment variable management |
| **Pillow (PIL)** | Loading and displaying weather icons |
| **OpenWeatherMap API** | Real-time weather data |

---

## 📂 Project Structure

```text
Python - Advance - Task4-Weather-App/
│
├── assets/
├── GUI.py
├── weather-api.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md