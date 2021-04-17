# random - библиотека по работе с генератором случайных чисел
# import random


# случаное целое число из диапазона (от, до) включительно
# запуская генерацию в цикле, создадим 10 случайных целых чисел от 0 до 100
# и напечатаем каждый из результатов в консоль

# for i in range(10):
#     some_random = random.randint(0, 100)
#     print("Случайное число от 0 до 100:", some_random)

# случайный элемент из объекта sequence
# for i in range(2):
#     names = ["Sergei", "Maxim", "Igor", "Pavel"]
#     print(random.choice(names))
    
# shuffle - перемешивание случайным образом
    
# random.shuffle(names)
# print("Перемешанный список:", names)

# подбрасывание монетки проще всего реализовать следущим образом
# for i in range(10):
#     print(random.choice(["Орёл", "Решка"]))

# создадим таблицу из случайных перелетов, для этого укажем исходные данные
# названия наших будущих колонок для Excel файла
xlsx_columns = ["Flight N", "Airline", "Airplane", "Departure",
                "Arrival", "Passengers", "Food"]

# данные, на основе которых будет генерироваться случайный перелёт
airlines = ["S7", "Aeroflot", "Ural", "Rossiya", "Azur", "Podeda"]
airplanes = [737, 747, 767, 777, 787]
airports = ["Omsk", "Kursk", "Msk", "Ufa", "Spb", "Sochi", "Tomsk", "Ekb"]
aircraft_capacity = [200, 550, 300, 400, 350]

import random

# функция генерирует случайный перелёт. Объявить ее нужно до вызова функции

def generate_flight():
    global i
    airline = random.choice(airlines)
    airplane = random.choice(airplanes)
    index_aircraft = airplanes.index(airplane)
    departure = random.choice(airports)
    arrival = random.choice(airports)
    while departure == arrival:
        arrival = random.choice(airports)
    passengers = random.randint(50, aircraft_capacity[index_aircraft])
    food = random.choice([True, True, False])
    return [i + 1, airline, airplane, departure, arrival, passengers, food]

# в цикле опрашиваем юзера о числе перелетов, до тех пор, пока он не введет
# корректные данные, требуемые от него (натуральное число)
while True:
    try:
        flights_amount = int(input("Enter amount of flights: "))
    except Exception:
        print("Try again")
        continue
    else:
        break
# пустой список, куда будут записываться случайные перелеты
data = []

# цикл генерирует случайные перелеты и записывает их в наш список
# цикл отрабатывает ровно столько раз, сколько перелетов указал ранее пользователь
for i in range(flights_amount):
    data.append(generate_flight())
    print(data[i])

# pandas - библиотека для работы с таблицами, с данными
import pandas as pd

# pandas имеет 2 типа данных и методы работы с ними
# dataseries - строка из таблицы - аналог одномерному списку
# dataframe - таблица - аналог двухмерному списку

# печатаем пустую строку, чтоб был небольшой отступ между 2 таблицами
# ранее мы печатали в консоль таблицу в формате list (64 строка)
print(" ")
# создаем объект dataframe из списка + указанных ранее колонок
df = pd.DataFrame(data, columns = xlsx_columns)
# печатаем наш объект dataframe в консоль
print(df)

# to_csv - сохранить файл в csv (можно также в Excel, формы записи немного отличаются)
# указывается сам файл df, указывается путь к файлу вместе с названием,
# а также нумеровать ли ряды. От нумерации отказываемся, так как имеем
# уникальный идентификатор ряда в виде колонки "Flight N"

while True:
    filename = input("Enter desired file name for dataset: ")
    if len(filename) > 2 and len(filename) < 10 and filename.isalpha():
        break
    print("Please specify name (3-9 symbols")

df.to_csv(f"{filename}({flights_amount}).csv", index = False, sep = ";")
df.to_excel(f"{filename}({flights_amount}).xlsx", index = False, sep = ";")

# путь к файлу указывается относительно текущего .py файла.
# если указываем лишь название файла, то csv файл будет сгенерирован в той же
# директории, где и находится исполняемый .py файл


