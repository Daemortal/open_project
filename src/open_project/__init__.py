"""
open_project Package

CLI tool for weather information powered by OpenWeatherMap API
"""

__version__ = "0.1.0"
__author__ = "Daemortal <daemortal@gmail.com>"

from .api import WeatherAPI, APIError
from .cli import main

__all__ = ['WeatherAPI', 'APIError', 'main']