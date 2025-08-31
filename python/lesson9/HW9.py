import requests
import pandas as pd

api_key = "BDTK6EPZLRWSURZT"
stock = "AAPL"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={api_key}'
response = requests.get(url)
data = response.json()

d = data['Time Series (Daily)']
df = pd.DataFrame.from_dict(d, orient="index") #Преобразование столбцов в строки
df.index = pd.to_datetime(df.index) # Преобразование в объект типа datetime для работы с временными рядами
df = df.map(pd.to_numeric) # Преобразование в числовой формат
df.head()
max_close = df['4. close'].max()
max_close_condition = df['4. close'] == max_close #Сравнение макс.знач. и ежедневного знач.закрыт.
print(max_close_condition)
max_close_data = df[max_close_condition]
missing_values = df.isnull().sum() #Сумма null'ов по столбцам
print(missing_values)
monthly_mean = df['4. close'].resample('ME').mean() # Получение ежемесячного среднего значения акций
print(monthly_mean)
df.to_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson9/stock_apple.csv', encoding='utf-8')
monthly_mean.to_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson9/monthly_mean_stock.csv', encoding='utf-8')


