🌤️ Advanced Weather App

Internship: Oasis Infobyte (OIBSIP)
Track: Python Development
Level: Advanced Tier
Task: Task 4 – Advanced Weather App

📌 Project Overview

The Advanced Weather App is a high-performance weather application developed as part of the Oasis Infobyte (OIBSIP) Python Development Internship.

The application fetches real-time weather information from the OpenWeatherMap API and presents it through a clean and user-friendly Graphical User Interface (GUI) built with Tkinter.

The app is designed with a focus on user experience, security, error handling, and clean software development practices. Users can search for any city around the world and view its current weather conditions, including temperature, humidity, weather descriptions, and visual weather icons.

✨ Features
🖥️ Interactive GUI
Built using Tkinter
Simple and intuitive interface
City input field for weather searches
Interactive Get Weather button
Dedicated weather results panel
Dynamically updates weather information

🌎 Real-Time Weather Data
Integrated with the OpenWeatherMap API
Retrieves live weather information
Supports cities from around the world
Uses Metric units (°C) for temperature

🌤️ Visual Weather Elements
Displays weather icons based on current conditions
Icons are stored in the /assets directory
Supports visual representations such as:
☀️ Sunny
☁️ Cloudy
🌧️ Rainy
⛈️ Thunderstorm
❄️ Snow
🌫️ Mist/Fog
🌡️ Detailed Weather Information

The application displays:

🌡️ Temperature
💧 Humidity
🌤️ Weather description
🏙️ City information
🖼️ Weather condition icon
⚠️ User-Friendly Error Handling

The application handles common API and user input errors without crashing the program.

Examples include:

City Not Found
Invalid city name
Missing API key
Network/API connection errors
Empty search input

Errors are displayed directly inside the GUI instead of appearing as terminal crashes.

🔐 Secure API Key Management

The OpenWeatherMap API key is never hardcoded into the Python source code.

Instead, the project uses:

.env for storing the API key
python-dotenv for loading environment variables
.gitignore to prevent .env from being uploaded to GitHub

This helps protect the API key from accidental exposure.

🛠️ Tech Stack
Technology	Purpose
Python 3.x	Main programming language
Tkinter	Graphical User Interface
Requests	API requests and networking
JSON	Processing API response data
python-dotenv	Secure environment variable management
Pillow (PIL)	Loading and displaying weather icons
OpenWeatherMap API	Real-time weather data

📂 Project Structure
Python - Advance - Task4-Weather-App/
├── GUI.py
├── weather-api.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Note: The .env file should never be committed to GitHub because it contains the private API key.

🧠 Logic & Implementation
1. API Integration — weather-api.py

The weather API module handles communication with the OpenWeatherMap API.

The application uses the requests library to send a request to the OpenWeatherMap endpoint.

The request uses Metric units, allowing temperatures to be displayed in Celsius.

The JSON response is then parsed to extract important information such as:

Temperature
Humidity
Weather condition
Weather description
City information

Example API workflow:

User enters city
       ↓
Application sends API request
       ↓
OpenWeatherMap processes request
       ↓
JSON weather response
       ↓
Application extracts required data
       ↓
GUI displays weather information
2. GUI & User Experience — GUI.py

The GUI provides the main interaction between the user and the application.

When the user enters a city and clicks Search/Get Weather:

The application reads the city name.
Previous weather results are cleared.
An API request is sent.
The returned JSON data is processed.
Weather information is extracted.
The appropriate weather icon is selected.
The GUI is dynamically updated with the latest information.

This creates a simple workflow where users do not need to interact with the terminal.

3. Security & Best Practices

The project follows basic security practices by keeping the API key outside the source code.

The API key is stored inside a .env file:

OPENWEATHER_API_KEY=your_key_here

Python loads the environment variable using python-dotenv.

The .env file should also be included in .gitignore:

.env

This prevents the API key from being accidentally pushed to GitHub.

🚀 How to Run
1. Clone the Repository

Clone the OIBSIP repository:

git clone https://github.com/SothSokhomal/OIBSIP.git

Navigate to the weather application folder:

cd "Python - Advance - Task4-Weather-App"
2. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

If you are using Python 3 and pip does not work, try:

pip3 install -r requirements.txt
3. Set Up the API Key

Create a .env file inside the project directory:

Python - Advance - Task4-Weather-App/
└── .env

Add your OpenWeatherMap API key:

OPENWEATHER_API_KEY=your_key_here

Replace your_key_here with your actual API key.

Important: Never share your API key publicly or commit the .env file to GitHub.

4. Run the Application

Start the application using:

python main.py

Or, if your system uses python3:

python3 main.py

🖼️ Application Workflow
┌─────────────────────────┐
│     Enter City Name     │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│     Click Get Weather   │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   OpenWeatherMap API    │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│      JSON Response      │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│    Parse Weather Data   │
└────────────┬────────────┘
             ↓
┌─────────────────────────┐
│   Display Results +     │
│      Weather Icon       │
└─────────────────────────┘
📋 Example Output

After searching for a city, the application can display information similar to:

📍 Phnom Penh

🌡️ Temperature: 30°C
💧 Humidity: 72%
🌤️ Condition: Clouds
☁️ Description: Scattered clouds

The weather icon is displayed alongside the information to provide a more visual experience.

🔒 Security Notes

For security reasons:

❌ Do not hardcode the API key in Python files.
❌ Do not upload .env to GitHub.
❌ Do not share your API key publicly.
✅ Store the API key in .env.
✅ Add .env to .gitignore.
✅ Load the API key using environment variables.
🎯 Learning Objectives

Through this project, the following skills were practiced:

Python GUI development with Tkinter
Working with REST APIs
Sending HTTP requests using requests
Processing JSON data
Environment variable management
API key security
Exception and error handling
Image handling with Pillow
Dynamic GUI updates
Organizing a Python project
Git and GitHub best practices

🏆 Internship Information

This project was completed as part of the:

Oasis Infobyte Internship Program (OIBSIP)

Track: Python Development
Task: Task 4
Project: Advanced Weather App
Level: Advanced Tier
👩‍💻 Author

Soth Sokhomal (Rose)

Python Development Intern
Oasis Infobyte (OIBSIP)

⭐ Project Status

Completed ✅

The application successfully demonstrates real-time weather API integration, GUI development, visual weather elements, error handling, and secure API key management.