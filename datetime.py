# Библиотеки - libraries
# import - для указания библиотеки
# import lib
# from lib import *
# from lib import lib1
# import library as lib
# import pandas as pd

# import matplotlib - библиотека для визуализации данных

from datetime import time, date, datetime, timedelta

# Сейчас в формате дата + время
datetime_object = datetime.now()
print("Сейчас:", datetime_object)

# Сегодня в формате даты
datetime_object = date.today()
print("Сегодня:", datetime_object)

# дата - формат, хранящий 3 объекта: год, месяц, число
any_date = date(2021, 10, 10)
print("Any date:", any_date)

# можно указывать параметры по имени
any_date = date(year = 2021, month = 1, day = 15)
print("15 Jan 2021:", any_date)

# дату можно раскладывать на составляющие (доступ к элементам формата даты)
print("На дворе",any_date.year, "год.")
print("Месяц:", any_date.month)
print("День:", any_date.day)

# время
some_time = time(10, 15, 35, 500)
print("Какое-то время:", some_time)

# не обязательно указывать параметры, по умолчанию они равны 0
midnight = time()
print("Время в полночь", midnight)

# можно указывать параметры по имени
some_time = time(hour = 10, minute = 25, second = 11)
print("Какое-то время:", some_time)

# также есть доступ к объектам внутри типа данных time
print(some_time.hour)
print(some_time.minute)
print(some_time.second)
print(some_time.microsecond)

# timedelta - тип данных для хранения разницы между датами/временем
start = date(2000, 1, 1)
delta = date.today() - start
print(delta, type(delta))



