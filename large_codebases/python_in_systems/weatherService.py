import requests

class WeatherService:
    api_key = 'you API key'
    base_url = f"https://api.openweathermap.org/data/2.5/forecast" #?q={city name}&appid={API key}
    @classmethod
    def getForecast(cls, city, country):
        full_url = cls.base_url + f"?q={city}&appid={cls.api_key}"
        reponse = requests.get(cls.base_url, params=[
            ('appid', cls.api_key),
            ('q', f'{city},{country}')
        ])
        data = reponse.json()
        return data['list']

if __name__ == "__main__":
    print(WeatherService.getForecast("Warsaw",  "Poland"))
    