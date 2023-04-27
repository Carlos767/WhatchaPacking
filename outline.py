import requests

# Function to get flight details from the user
def get_flight_itinerary():
    departure_city = input("Enter departure city: ")
    destination_city = input("Enter destination city: ")
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    return departure_city, destination_city, departure_date

# Function to look up flights using a hypothetical flight API
def get_flights(departure_city, destination_city, departure_date):
    # Replace with actual flight API endpoint and parameters
    api_endpoint = "https://api.example.com/flights"
    params = {
        "departure_city": departure_city,
        "destination_city": destination_city,
        "departure_date": departure_date
    }
    response = requests.get(api_endpoint, params=params)
    flights = response.json()
    return flights

# Function to check weather at the destination using a hypothetical weather API
def check_weather(destination_city):
    # Replace with actual weather API endpoint and parameters
    api_endpoint = "https://api.example.com/weather"
    params = {
        "city": destination_city
    }
    response = requests.get(api_endpoint, params=params)
    weather = response.json()
    return weather

# Function to make suggestions on what to pack based on weather
def make_packing_suggestions(weather):
    temperature = weather["temperature"]
    conditions = weather["conditions"]

    if temperature < 10:
        return "It's cold at your destination. Remember to pack warm clothes, including a coat, hat, and gloves."
    elif temperature >= 10 and temperature < 20:
        return "It's cool at your destination. Pack some light jackets or sweaters."
    elif temperature >= 20 and temperature < 30:
        return "It's mild at your destination. You'll need some light clothes like t-shirts and shorts."
    else:
        return "It's hot at your destination. Pack lightweight clothes like shorts, dresses, and sunscreen."

# Main program
def main():
    print("Welcome to the Flight Planner!")
    departure_city, destination_city, departure_date = get_flight_itinerary()
    flights = get_flights(departure_city, destination_city, departure_date)
    if flights:
        print("Here are the available flights:")
        for flight in flights:
            print(f"Flight {flight['flight_number']} - Departure: {flight['departure_time']}, Arrival: {flight['arrival_time']}")
    else:
        print("No flights found.")

    weather = check_weather(destination_city)
    if weather:
        print("Here's the weather at your destination:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Conditions: {weather['conditions']}")
        suggestions = make_packing_suggestions(weather)
        print("Packing Suggestions:")
        print(suggestions)
    else:
        print("Failed to get weather information.")

if __name__ == "__main__":
    main()
