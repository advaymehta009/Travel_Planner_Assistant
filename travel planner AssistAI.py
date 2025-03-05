import openai
import requests

# Sample API keys (Replace with actual keys)
OPENAI_API_KEY = "your_openai_api_key"
HOTEL_API_KEY = "your_hotel_api_key"
MODERATION_API_KEY = "your_moderation_api_key"
DATABASE_API_KEY = "your_database_api_key"

openai.api_key = OPENAI_API_KEY

# System Design: Breaking the workflow into structured stages

def findBestHotels(destination):
    """Find the best 5 hotels for a given destination."""
    url = f"https://api.example.com/hotels?location={destination}&apikey={HOTEL_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        hotels = response.json()
        return [hotel['name'] for hotel in hotels[:5]]
    return ["No hotels found"]


def generate_itinerary(destination, days, interests=None):
    """Generate a personalized itinerary for the given destination and duration."""
    itinerary = f"Suggested {days}-day itinerary for {destination}"
    if interests:
        itinerary += f" based on your interest in {interests}"  
    return itinerary

# Implementing Safety Measures
def moderate_content(user_input):
    """Check for potentially unsafe or sensitive content."""
    moderation_response = openai.Moderation.create(
        input=user_input,
        api_key=MODERATION_API_KEY
    )
    if moderation_response['results'][0]['flagged']:
        return "Your request contains unsafe content and cannot be processed."
    return None

# Extracting User Intent
def extract_intent(user_input):
    """Extract user intent and relevant details from their request."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Identify the user's intent from the following message."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']


def call_function_api(messages):
    """Leverage Function Calling API to manage chatbot responses."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=messages,
        functions=[
            {
                "name": "findBestHotels",
                "description": "Find the best 5 hotels for a given destination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {"type": "string", "description": "The desired travel destination"}
                    },
                    "required": ["destination"]
                }
            },
            {
                "name": "generate_itinerary",
                "description": "Generate an itinerary for a given destination and duration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {"type": "string"},
                        "days": {"type": "integer"},
                        "interests": {"type": "string"}
                    },
                    "required": ["destination", "days"]
                }
            }
        ]
    )
    return response['choices'][0]['message']


def travel_planner(user_input):
    """Main function to initiate the travel planning conversation."""
    # Check for unsafe content
    moderation_result = moderate_content(user_input)
    if moderation_result:
        return moderation_result
    
    # Extract user intent
    user_intent = extract_intent(user_input)
    
    messages = [
        {"role": "system", "content": "You are a helpful travel planner. Use a structured format to present information."},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": "Certainly! Let me fetch the best options for you."}
    ]
    
    response_message = call_function_api(messages)
    function_name = response_message.get("function_call", {}).get("name")
    
    if function_name == "findBestHotels":
        destination = response_message.get("function_call", {}).get("arguments", {}).get("destination")
        result = findBestHotels(destination)
    elif function_name == "generate_itinerary":
        destination = response_message.get("function_call", {}).get("arguments", {}).get("destination")
        days = response_message.get("function_call", {}).get("arguments", {}).get("days")
        interests = response_message.get("function_call", {}).get("arguments", {}).get("interests")
        result = generate_itinerary(destination, days, interests)
    else:
        result = "Unable to process request."
    
    # Ensure Output Consistency
    formatted_response = f"**Travel Plan:**\n\n{result}"
    return formatted_response

# Example usage
def test_travel_planner():
    test_cases = [
        "Help me find the perfect hotel in Paris.",
        "Find the best 5 hotels for California."
    ]
    
    for query in test_cases:
        print(f"Query: {query}")
        print(travel_planner(query))
        print("-" * 50)

test_travel_planner()
