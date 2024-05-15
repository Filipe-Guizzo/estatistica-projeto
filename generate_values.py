# Temperatura, Precipitação, Umidade, Estação do ano, Vento

import pandas as pd

def find_values(month: str, city: str):

    # Lendo o arquivos csv
    df_precipitation = pd.read_csv('./csv/precipitacao.csv', on_bad_lines='skip', sep=';')
    df_temperature = pd.read_csv('./csv/temperatura.csv', on_bad_lines='skip', sep=';')
    df_humidity= pd.read_csv('./csv/umidade.csv', on_bad_lines='skip', sep=';')
    df_wind = pd.read_csv('./csv/vento.csv', on_bad_lines='skip', sep=';')

    # Obtendo a precipitacao
    df_precipitation = df_precipitation.query(f'CIDADE == "{city}"')
    precipitation = df_precipitation[month].values[0]

    # Obtendo a temperatura
    df_temperature = df_temperature.query(f'CIDADE == "{city}"')
    temperature = df_temperature[month].values[0]

    # Obtendo a umidade
    df_humidity = df_humidity.query(f'CIDADE == "{city}"')
    humidity = df_humidity[month].values[0]

    # Obtendo o vento
    df_wind = df_wind.query(f'CIDADE == "{city}"')
    wind = df_wind[month].values[0]

    return {
        'month': month,
        'precipitation': precipitation,
        'temperature': temperature,
        'humidity': humidity,
        'wind': wind    
    }

