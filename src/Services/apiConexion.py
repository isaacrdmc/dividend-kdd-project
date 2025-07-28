import pandas as pd
import requests as re
import os
from dotenv import load_dotenv
import json

# ? Vamos a realizar la peticion con request:

# * Cargamos la API KEY desde '.env':
load_dotenv()
API_KEY = os.getenv('KEY_API')
# APO_URL = os.getenv('URL_API')


# ^ Ahora creamos la funcion para la petición:
# * COmo parametro recibimos el nombre de la empresa a analizar
def obtenerDividendos(symbol):
    url = "https://www.alphavantage.co/query"
    # url
    params = {
        "function": "DIVIDENDS",
        "symbol": symbol,
        "apikey": API_KEY
    }

    # * Realizamos la petición a la API y le pasamos el cuerpo
    # response = re.get(url, params=params)
    response = re.request("GET", url, params=params)

    # * 
    if response.status_code == 200:
        data = response.json()
        print(f"Datos obtenidos para la empresa {symbol}: ")
        return print(json.dumps(data, indent=4))
    else: 
        print(f"Error al obtener los datos para la empresa {symbol}. Código de error: {response.status_code}")
        return None
    


# ? Ejecutamos el script:
if __name__ == "__main__":
    simbolo = "AAPL"
    datos = obtenerDividendos(simbolo)

    if datos:
        print(datos)
