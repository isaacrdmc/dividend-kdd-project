from src.Services.apiConexion import obtenerDividendos
from src.Services.bdConexion import getEngine
from src.Scripts.extraccion import insertarRaw


# ? Ejecutamos el código:
if __name__ == "__main__":
    engine = getEngine()
    symbol = "MSFT"

    datos = obtenerDividendos(symbol)
    insertarRaw(datos, engine, symbol)


