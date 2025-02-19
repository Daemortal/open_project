import requests
from typing import Dict, Union

class APIError(Exception):
    """Base exception for API errors"""
    pass

class WeatherAPI:
    def __init__(self, api_key: str):
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.api_key = api_key

    def get_current_weather(
        self,
        city: str,
        units: str = 'metric'
    ) -> Dict[str, Union[str, float]]:
        """
        Fetch current weather data
        
        Args:
            city: City name and country code (e.g., 'London,GB')
            units: Measurement system (metric/imperial)
        
        Returns:
            Dictionary with weather data
            
        Raises:
            APIError: On any API request failure
        """
        try:
            response = requests.get(
                f"{self.base_url}/weather",
                params={
                    'q': city,
                    'units': units,
                    'appid': self.api_key
                },
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            return self._parse_response(data, units)
            
        except requests.exceptions.RequestException as e:
            raise APIError(f"Weather API request failed: {str(e)}")

    def _parse_response(
        self,
        data: dict,
        units: str
    ) -> Dict[str, Union[str, float]]:
        """Parse raw API response into standardized format"""
        return {
            'city': data.get('name', 'N/A'),
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].capitalize(),
            'units': '°C' if units == 'metric' else '°F',
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure']
        }