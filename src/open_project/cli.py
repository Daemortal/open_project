import click
from typing import Optional
from .api import WeatherAPI, APIError

@click.command()
@click.option('--city', required=True, help='City name (e.g. "London,GB")')
@click.option('--api-key', envvar='OWM_API_KEY', help='OpenWeatherMap API key')
@click.option('--units', default='metric', type=click.Choice(['metric', 'imperial']))
@click.option('--full', is_flag=True, help='Show detailed weather information')
def main(city: str, api_key: Optional[str], units: str, full: bool):
    """Weather-Tea - Command Line Weather Interface"""
    
    if not api_key:
        raise click.ClickException(
            "API key required (use --api-key or OWM_API_KEY environment variable)"
        )
    
    try:
        weather = WeatherAPI(api_key)
        data = weather.get_current_weather(city, units)
        
        click.secho(f"\n?? Weather in {data['city']}:", fg='cyan')
        click.echo(f"  Temperature: {data['temp']}{data['units']}")
        click.echo(f"  Feels like: {data['feels_like']}{data['units']}")
        click.echo(f"  Conditions: {data['description']}")
        
        if full:
            click.echo("\nAdditional details:")
            click.echo(f"  Humidity: {data['humidity']}%")
            click.echo(f"  Wind Speed: {data['wind_speed']} m/s")
            click.echo(f"  Pressure: {data['pressure']} hPa")
            
        click.echo()
        
    except APIError as e:
        raise click.ClickException(str(e))