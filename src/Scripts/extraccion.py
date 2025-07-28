
import pandas as pd


# ? Creamos la funcion para
def insertarRaw(data, engine, symbol):

    if not data:
        print("No hay suficientes datos para insertar")
        return
    
    # ? 
    df = pd.DataFrame(data)
    df['symbol'] = symbol
    df.to_sql('dividendos_raw', con=engine, if_exists='append', index=False)
    print(f"Datos insertados {len(df)} registros de {symbol} ")


