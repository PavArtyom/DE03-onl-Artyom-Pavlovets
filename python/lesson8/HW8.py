import pandas as pd
import numpy as np

"""
Выполнить анализ набора данных (прилагается к занятию), аналогично выполненному на занятии, 
и подготовить отчет.
"""

df = pd.read_csv(r'/Users/usermac/DE03-onliner-Artyom-Pavlovets/python/lesson8/customers.csv')

df['purchase_amount'] = np.random.randint(1000, 8500, size=len(df)) #Добавление столбца покупок
date_column = pd.date_range(start='2025-01-01', end='2025-01-20', freq='D')
df['date_of_last_purchase'] = date_column #Добавление столбца дат
print(df)
mean_purchase_amount = df['purchase_amount'].mean() #Средняя сумма покупок за месяц
print(f'Средняя сумма покупок:{mean_purchase_amount}')

rich_customers = df[df['purchase_amount'] > 7000] #Клиенты,которые совершили покупки на сумму более 7000
print(f'Топ клиенты:{rich_customers}')

not_rich_customers = df[df['purchase_amount'] < 3000] #Клиенты,которые совершили покупки на сумму менее 3000
print(f'Клиенты.которых стоит мотивировать:{not_rich_customers}')

profit_for_month = np.sum(df['purchase_amount']) #Общая сумма покупок
print(f'Прибыль за месяц:{profit_for_month}')

std_dev_amount = np.std(df['purchase_amount'])
print(f'Стандартное отклонение в столбце purchese_amount:{std_dev_amount}') #Стандартное отклонение

median_amount = np.median(df['purchase_amount']) # медианное значение
print(f'Медианное значение:{median_amount}')

top_list_of_cust = df.sort_values(by='purchase_amount', ascending=False) #Сортировка по убыванию
print(f'Сортировка клиентов:{top_list_of_cust}')


