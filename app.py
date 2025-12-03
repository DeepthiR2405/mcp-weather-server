from fastapi import FastAPI
import requests

app = FastAPI(title="MCP Weather Server")

@app.get("/")
def root():
    return {"message": "MCP Weather Server is running"}

@app.get("/weather")
def get_weather(city: str):
    API_KEY = "YOUR_API_KEY_HERE"  # Replace

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        return {"error": "Unable to fetch weather"}

    data = res.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }


