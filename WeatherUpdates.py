import python_weather
import asyncio

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.find("Warsaw")

    print(weather.current.temperature)

    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())