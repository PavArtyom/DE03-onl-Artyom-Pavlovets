from ingestion import load_dataframe_from_csv


file_path = '/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson10/orders.csv'

df = load_dataframe_from_csv(file_path)

if df is not None:
    print("Файл успешно загружен!")
    print(df)
else:
    print("Не удалось загрузить файл.")

missing_values = df.isnull().sum() # Проверка NaN
print(missing_values)

valid_data_of_price = df[(df['unit_price'] > 0)] # Проверка стоимости товара больше 0
valid_data_of_shipping_cost = df[(df['shipping_cost'] >= 0)] # Проверка стоимости доставки больше 0
# print(valid_data_of_shipping_cost)
# print(valid_data_of_price)




