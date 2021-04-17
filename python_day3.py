
#  Exception - исключения

var1 = 5
var2 = 0

# result = var1 / var2 - ZeroDivisionError

input1 = "abc"

# print(int(input1) ** 2) - ValueError

# try - except - else - finally

list1 = [1, 2, 3, 4, 5]
# print("7th element is:", list[6]) - TypeError

try:
    x = 5 / 1
    y = 7 / 3
except ZeroDivisionError:
    print("Нельзя делить на нуль")
except ValueError:
    print("Нельзя конвертировать текст в int")
except TypeError:
    print("Обращение по несуществующему индексу")
except Exception:
    print("Что-то другое произошло")
else:
    print("Ни один из exceptions не сработал, блок try отработал")
finally:
    print("А вот это исполняется всегда")

# raise - поднять - заставить сработать исключение

# input1 = int(input("Введи, что поделить? "))
# input2 = int(input("Введи, на что поделить? "))
# if input2 == 0:
#     raise ZeroDivisionError("Ты что, хочешь поделить на " + str(var1) + " ?")


# import random
# target = random.randint(0, 100)
# guess = 0
# attempts = 0

# while guess != target:
#     if attempts == 7:
#         print("Игра окончена")
#         break
#     try:
#         guess = float(input("Угадай моё число от 0 до 100: "))
#     except Exception:
#         attempts += 1
#         print("Ты ввел не число, а текст. Попыток:", attempts)
#         continue
#     if guess > 100 or guess < 0:
#         attempts += 1
#         print("Ты указал число больше 100, или меньше 0. Попыток:", attempts)
#         continue
#     if guess > target:
#         attempts += 1
#         print("Попробуй поменьше. Попыток:", attempts)
#     elif guess < target:
#         attempts += 1
#         print("Попробуй побольше. Попыток:", attempts)

# else:
#     print("Ты угадал!")


# functions - функций
# объявление функций - def func(): затем отступ с исполнительным блоком
# func() - вызов функции (в скобках можно передать параметры)
# def hello_world(y_name):
#     global name
#     name = "Alex"
#     print("Hello", y_name)

# name = "Igor"
# x_name = "Sergei"
# hello_world(x_name)
# print(x_name)
# print(name)

# return - вернуть объект(ы), обработанные в функции
# def PlusFive(value):
#     y = 0
#     print("You entered number:   ", value)
#     value = value + 5
#     print("Your number plus 5 is:", value)
#     if y == 0:
#         return value
#     else:
#         return 0

#     print("А вот это не должно было напечататься")

# x = PlusFive(7)
# print("Your number plus 5 is:", x)


# можно передавать несколько парамтров
# параметры передаются в том порядке, в котором они указаны
# можно указывать свой порядок, если мы знаем, имена аргументов функции
# функции могут иметь значения "по умолчанию"
def summa(a = 3, b = 3, c = 2):
    return a + 10 * b + 100 * c

# print(summa(c = 1, a = 2, b = 3))
# print(summa())


# если не знаем число аргументов
# *args **kwargs
    
# def new_sum(*elem, k = 0, g = 5):
#     print(elem)
#     result = 0
#     for i in elem:
#         result += i
#     result *= k
#     return result

# print(new_sum(1, 2, 3, 4))

def func(**kid):
    pass
    
