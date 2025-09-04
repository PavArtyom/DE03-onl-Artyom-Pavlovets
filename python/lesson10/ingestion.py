import pandas as pd

def load_dataframe_from_csv(filepath):
    try:
        df = pd.read_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/orders.csv')
        return df
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {filepath}")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
