# импортируем библиотеку
import pandas as pd

# создаем объект df из импортированного файла
df = pd.read_csv("Flights(100).csv")

# убеждаемся, что все работает
print(df)

# вывод не всей таблицы
# df.head(num) - вывод num первых строк
print(df.head(10))

# df.tail(num) - вывод num последних строк
print(df.tail(10))

# df = df.head(10) - показывает, что df.head лишь создает временный объект,
# сам df при этом не изменяется. Чтоб обрезать объект df до 10 строк,
# необходимо записать df = df.head(...)

# df.columns - показ колонок
print(df.columns)

# df.describe() - показывает описание (только для нумерических колонок)
print(df.describe())

print(" ")
# df.info() - показывает информация о таблице
print(df.info())

# df.columns[] - доступ к колонкам
print(df.head(10)["Passengers"])

# несколько колонок выводить тоже можно
print(df[["Airline", "Airplane"]])

# доступ к рядам [start:stop:step]
print(df.iloc[15:25:2])

# sort_values - сортировка
df = df.sort_values("Passengers", ascending = False)
print(df.head(10))

#бывают такие ловушки
# print("1010000000000" > "21")
# print(1010000000000 > 21)

# добавление новой колонки
business_passengers = (df["Passengers"] * 30) // 100
df["Business"] = business_passengers
print(df)

# удаление колонки
df = df.drop(columns = ["Business"])
print(df.head(10))
