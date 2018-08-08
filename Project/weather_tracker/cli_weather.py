
import requests
import click

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location,api_key=SAMPLE_API_KEY):
    url = 'http://samples.openweathermap.org/data/2.5/weather'
    query_params = {
        'q':location,
        'appid':api_key,
    }
    response = requests.get(url,params = query_params)
    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
@click.option('--h','-a',help='Your Optional Parameter')
def main(location,h):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. Kathmandu
    2. London

    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    weather = current_weather(location)
    print(f"The weather in {location} is {weather}")
    if h is not None:
        print(f'You passed {h} as optional parameter')

if __name__ == "__main__":
    main()