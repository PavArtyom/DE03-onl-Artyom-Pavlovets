from ingestion import load_dataframe_from_csv
import pandas as pd

file_path = '/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/orders.csv'

df = load_dataframe_from_csv(file_path)

if df is not None:
    print("Файл успешно загружен!")
    print(df)
else:
    print("Не удалось загрузить файл.")

df.order_date = pd.to_datetime(df.order_date) #Преобразование в формат даты для работы с временными рядами
# print(df.dtypes)

df['total_cost'] = df['unit_price'] * df['quantity'] * (1 - df['discount']) + df['shipping_cost']
total_profit = df['total_cost'].sum()
print(f'Общая прибыль: {total_profit}')
df['pure_profit'] = df['total_cost'] * (1 - df['returned']) # прибыль с учетом возвратов
net_revenue = df['pure_profit'].sum()
print(f'Чистая прибыль:{net_revenue}')
df['order_value'] = df['unit_price'] * df['quantity']
avg_order_value = df.groupby('order_date')['order_value'].sum().mean() # Средний чек
print(f'Средний чек: {avg_order_value}')

sales_by_city = df.groupby('city')['order_value'].sum() # Сумма по каждому отдельному городу
print(f'Продажи по городам:{sales_by_city}')

richest_cities = sales_by_city.nlargest(5) # Топ 5 городов по выручке
print(f'Топ 5 городов по выручке: {richest_cities}')

top_product_profit = df.groupby('product')['order_value'].sum().nlargest(5)
print(f'Топ прибыль по категориям: {top_product_profit}')

return_percentage = df['returned'].mean() * 100
print(f'Процент возвратов:{return_percentage}')

returns_by_each_product = df.groupby('product')['returned'].sum().nlargest(5)
print(f'Топ 5 самых возвращаемых товаров по категориям: {returns_by_each_product}')

df['3_day_rolling_mean'] = df['order_value'].rolling(window=3).mean() # Cкользящее среднее за 3 дня
df['3_day_rolling_mean'] = df['3_day_rolling_mean'].fillna(0) # Заполняем значения NaN - 0

top_product_profit.to_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/top_product_profit.csv', encoding='utf-8')
sales_by_city.to_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/sales_by_city.csv', encoding='utf-8')
returns_by_each_product.to_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/returns_by_each_product.csv', encoding='utf-8')