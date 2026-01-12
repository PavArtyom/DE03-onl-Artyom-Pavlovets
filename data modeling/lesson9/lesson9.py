'''
У вас есть два CSV-файла: employees_north.csv с сотрудниками северного региона и employees_south.csv с
сотрудниками южного региона. Используя Python, прочитайте оба файла и объедините данные в одну таблицу.
После объединения нужно очистить данные от сотрудников, у которых нет указанного адреса электронной почты
(пустое значение или пропуск). Затем необходимо выделить сотрудников,
у которых должность содержит слово “Manager” (без учёта регистра),
и сохранить их в отдельный файл managers.csv.
Оставшихся сотрудников сохраните в файл regular_staff.csv. Все файлы должны быть сохранены в формате CSV.
'''

import pandas as pd

df1 = pd.read_csv("employees_north.csv")
df2 = pd.read_csv("employees_south.csv")

df3 = pd.concat([df1, df2], ignore_index = True)

employees = df3.dropna(subset = ["email"])

managers = employees[employees["position"].str.contains("Manager", case = False)]

managers.to_csv("managers.csv", index = False)

rest_employees = employees[~employees["position"].str.contains("manager", case = False)]

rest_employees.to_csv("regular_staff.csv", index = False)


