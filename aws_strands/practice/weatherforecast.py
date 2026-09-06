from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request


WEATHER_SYSTEM_PROMPT = """
You are a weather assistant with HTTP capabilities.

You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:

1. First get coordinates using:
   https://api.weather.gov/points/{latitude},{longitude}

2. Then use the returned forecast URL to get the actual forecast.

Always explain weather conditions clearly and provide context.
"""


model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2"
)

weather_agent = Agent(
    model=model,
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[http_request]
)


if __name__ == "__main__":
    print("\nWeather Forecaster Strands Agent")
    print("Running locally with Ollama\n")
    print("Ask about weather in any US location.")
    print("Type 'exit' to quit.")

    while True:
        try:
            user_input = input("\n> ")

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = weather_agent(user_input)

            print(str(response))

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        except Exception as e:
            print(f"\nError: {str(e)}")