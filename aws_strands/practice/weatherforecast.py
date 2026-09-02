from strands import Agent
from strands.models.bedrock import BedrockModel
from strands_tools import http_request

WEATHER_SYSTEM_PROMPT = """
You are a weather assistant with HTTP capabilities. You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get coordinates using https://api.weather.gov/points/{latitude},{longitude}
2. Then use the returned forecast URL to get the actual forecast

Always explain weather conditions clearly and provide context for the forecast.
"""

# ✅ Using Mumbai region (closest to you in India!)
model = BedrockModel(
    model_id="amazon.nova-pro-v1:0",
    region_name="ap-south-1"  # Mumbai 🇮🇳
)

weather_agent = Agent(
    model=model,
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[http_request]
)

if __name__ == "__main__":
    print("\nWeather Forecaster Strands Agent\n")
    print("Running on AWS Mumbai Region (ap-south-1) 🇮🇳")
    print("\nAsk about weather in any US location:")

    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            response = weather_agent(user_input)
            print(str(response))
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try a different request.")
