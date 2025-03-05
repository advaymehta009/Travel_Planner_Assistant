# Travel Planner Assistant

## Overview
Travel Planner AI is an intelligent assistant that helps users plan their trips efficiently by providing hotel recommendations and generating personalized itineraries. It leverages OpenAI's GPT-4-Turbo with function calling and integrates external APIs to deliver accurate and structured travel planning assistance.

## Features
- **Find Best Hotels:** Recommends top 5 hotels based on the destination.
- **Generate Itineraries:** Creates a custom travel plan based on user preferences.
- **AI-Powered Interaction:** Extracts user intent for seamless conversation.
- **Safety Measures:** Uses content moderation to filter inappropriate inputs.
- **API Integration:** Fetches real-time hotel data from external sources.

## Installation
### Prerequisites
- Python 3.8+
- OpenAI API Key
- External Hotel Listings API Key

### Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/travel-planner-ai.git
   cd travel-planner-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   export HOTEL_API_KEY="your_hotel_api_key"
   ```
4. Run the application:
   ```bash
   python travel_planner.py
   ```

## Usage
### Example Queries
- **Find hotels:** "Help me find the perfect hotel in Paris."
- **Plan itinerary:** "Create a 3-day itinerary for Rome with historical sites."

## System Architecture
1. **User Input Processing:**
   - Checks for unsafe content using the Moderation API.
   - Extracts intent using OpenAI GPT-4-Turbo.
2. **Function Calling API:**
   - Determines whether to call `findBestHotels` or `generate_itinerary`.
   - Fetches data from external APIs.
3. **Response Generation:**
   - Formats responses in a structured and user-friendly manner.

## Challenges & Solutions
### Challenges:
- **Handling API Rate Limits** → Implemented caching for repeated queries.
- **Extracting User Intent** → Optimized prompt engineering for accuracy.
- **Output Consistency** → Standardized response formatting.

### Lessons Learned:
- Function calling significantly improves chatbot efficiency.
- Moderation layers enhance user safety and experience.
- Clear system architecture ensures maintainability and scalability.

## Future Enhancements
- Multi-city itinerary support.
- Real-time travel updates.
- Integration with flight and activity booking services.

## License
- N/A

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve Travel Planner AI.

## Contact
For any queries, reach out to [advaymehta009@gmail.com](mailto:advaymehta009@gmail.com).

