# -*- coding: utf-8 -*-
"""

"""

# Это однострочный комментарий
# Вторая строчка комментария
# Ctrl + 1 - горячая клавиша для комментирования

# """ """ для аннотации ( лучше использовать единожды)

# 4 категории данных (основные)
# 1) numeric - нумерическая категория

# "=" - оператор присваивания
# "==" - оператор сравнения
# integer - целочисленные данные
integer1 = 5
integer2 = 2
# print - оператор вывода в консоль
print(integer1)
# type(x) - вычисление типа данных
print(type(integer1))
# операции с numeric
# + - * / ** // %
# сумма
print(integer1 + integer2)
# разность
print(integer1 - integer2)
# умножение
print(integer1 * integer2)
# деление
print(integer1 / integer2)
#  возведение в степень
print(integer1 ** integer2)
# деление с отбрасыванием остатка
print(integer1 // integer2) 
# остаток от деления
print(integer1 % integer2)

# float - число с плавающей точкой
float1 = 4.5
print(type(float1), float1)

# complex - комплексные числа
compl = 2 + 3j
print(type(compl), compl)


# 2) sequence - тип данных "последовательность"
# string - строка
string1 = "Hello World"
string2 = 'Another "Hello World" One'

print(type(string2), string2)
print("integer1 is equal to", integer1)

# операции со строками
# + * 
print(string1 + " " + string2)
print((string1 + " ")* 3)

# доступ к элементу [i]
print("First element in string1 is:", string1[0])
print("Last element in string1 is:", string1[-1])

# доступ к нескольким элементам [i:j]
print("First 5 elements in string1:",string1[0:5])

# доступ к диапазону с шагом [i:j:k]
print("Четные элементы:", string1[-1:0:-2])

# значения по умолчанию
# [start:stop:step]
# start = 0; stop = "до конца включительно"; step = 1
print("Попытка:", string1[1::3])
# help(type) - выводит справку
# help(str)

# "\a" - звук
# print("\a")

# a in b - генерирует True/False (проверка на наличие в строке)
b = "Boeing"
print("B" in b, "Bo" not in b)

# list - список (можно хранить данные в любом количестве, любых типов)
list1 = [1, 2, 3, b]
print("list1 type is:", type(list1), ", list1 has:", list1)

# доступ по индексам работает так же, как и со строками
print("Last element in list1 is:", list1[-1])

# len(list1) - длина объекта sequence
print("list1 lenght is:", len(list1))

# append - добавить в конец
list1.append("Sergei")
print("New list1 is:", list1)

# insert - добавить в конкретное место
list1.insert(1, True)
print("New list1 is:", list1)

# remove - удалить из списка по значению
list1.remove("Boeing")
print("New list1 is:", list1)

# pop - удалить из списка по индексу
list1.pop(-2)
print("New list1 is:", list1)

# reverse - развернуть список в обратном порядке
list1.reverse()
print("New list1 is:", list1)

# index - возвращает индекс по значению
print("True is on",list1.index(True), "position")

# sort - сортировка
# если строки - сортировка по алфавиту
# если числа - сортировка по возрастанию
list_of_names = ["1","Sergei", "Maxim", "Igor", "Ivan", "Fedor"]
list_of_names.sort(key = len, reverse = True)
print("Sorted names list:", list_of_names)

list_of_numbers = [1, 7, 15, 29, 2, 4, 3, 17, 10]
list_of_numbers.sort()
print("Sorted numbers list:", list_of_numbers)
print("1" < "9" < "A" < "a" < "А" < "а")

# tuple - кортеж - это тот же список, только иммутабельный
tuple1 = (1, 2, 3)
# tuple1.append(1) - методы с .(модификация сущестующего - невозможна)
print("First Element in tuple is:",tuple1[0])
tuple2 = tuple1 + (1,)
print(tuple2)

clients = [(1, 2), (3, 4), (5, 6)]
print(list1)
clients.append((7, 8))
print(list1)

# range() - создание итератора
print("Range 0 to 10 is:", range(1, 10, 2), "Range type is:", type(range(10)))

# 3) container
# set - сет - последовательность без дубликатов
set1 = {1, 2, 3, 4, 5, 1, 3, 5, 7}
print("Set type is:", type(set1), "Set1 is:", set1)

# dict - словарь - список из пар (key + value)
dict1 = {"bananas": 15, "oranges": "Sweet", "melons": 13}
print("Fruits We have:", dict1)
print("Dictionary type is:", type(dict1))

# update - добавляет объект в словарь
dict1.update({"apples": 6})
print("Fruits We have:", dict1)

# добавление объекта с существующим ключом перезапишет его value
dict1.update({"oranges": 7})
print("Fruits We have:", dict1)

# pop также удаляет элемент по ключу
dict1.pop("melons")
print("Fruits We have:", dict1)


# 4) other

# boolean - True or False
fact1 = True
fact2 = False
print(10 == 9)

# boolean операции + (or) * (and) ! (not)
print("True and False is:", fact1 and fact2)
print("True or False is:", fact1 or fact2)
print("True and False is:", fact1 and not fact2)
print("Boolean type is:", type(fact1))

# None - Nonetype - пустышка, пустота, аналог null

winner = None
print("NoneType is:", type(winner), "None value is:", winner)
print(None == None)

# конвертация типов - возможно, только если это очевидно
# a = 5.5
# a = int(a)
# print(a)

# fibonacci series
a = 1
b = 1
for i in range(10):
    a, b = b, a + b
    print(a)



