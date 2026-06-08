import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            
            print("\n===== Weather Report =====")
            print(f"Location   : {city_name}, {country}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity   : {humidity}%")
            print(f"Condition  : {condition.capitalize()}")
            print("==========================")
        else:
            print("City not found! Please check the city name.")
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")

# Main program
print("===== Basic Weather App =====")

api_key = "ff293a2fe0e64df53cc1208ab27d5a17"

while True:
    city = input("\nEnter city name (or 'exit' to quit): ")
    if city.lower() == "exit":
        print("Goodbye!")
        break
    get_weather(city, api_key)
