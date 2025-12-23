import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
}


class ForeCastRepository:
    GET_COORD_URL = 'https://geocoding-api.open-meteo.com/v1/search'
    WEATHER_FORECAST_URL = 'https://api.open-meteo.com/v1/forecast'

    def find_city(self, city_name: str, language: str) -> dict:
        """ Функция возвращает данные городов, подходящих под заданное имя города """
        params = {
            'name': city_name,
            'language': language,
        }

        try:
            response = requests.get(
                url=self.GET_COORD_URL,
                headers=headers,
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            response_data = response.json()

            if not response_data.get('results'):
                raise requests.exceptions.HTTPError()

        except requests.exceptions.HTTPError:
            raise ValueError('Ошибка при запросе получения координат города')
        except requests.exceptions.ReadTimeout:
            raise ValueError('Ошибка по тайм-ауту запроса получения координат города')
        except Exception:
            raise ValueError('Неизвестная ошибка при запросе получения координат города')
        else:
            return response_data

    def get_temperature_by_geo_coord(self, latitude: str, longitude: str, hourly: str) -> dict:
        """ Функция отправляет запрос на получение температур, по заданным координатам, на неделю """
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'hourly': hourly,
        }

        try:
            response = requests.get(
                url=self.WEATHER_FORECAST_URL,
                headers=headers,
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            response_data = response.json()

        except requests.exceptions.HTTPError:
            raise ValueError('Ошибка при запросе данных о погоде города')
        except requests.exceptions.ReadTimeout:
            raise ValueError('Ошибка по тайм-ауту запроса данных о погоде города')
        except Exception:
            raise ValueError('Неизвестная ошибка при запросе данных о погоде города')
        else:
            return response_data
