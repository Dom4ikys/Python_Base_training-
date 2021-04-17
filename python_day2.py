# if/elif/else conditions - условные операторы

# if условие 1:
#   блок действий 1
# elif условие 2:
#   блок действий 2
# .........
# else:
#   блок действий n    

x = 5
y = 5
if x == 5 and y == 5:
    print("x = 5")
    print("Ветка 2")
    if y == 5:
        print("y = 5")
elif x > 5:
    print("x > 5")
    print("Ветка 2")
else:
    print("x < 5")
    print("Ветка 3")

# минимальная конструкция - if.
if x == 5:
    print(x)

# input - спрашиваем у пользователя программы информацию
# эта информация сохраняется в переменную в виде строки

in1 = input("Please enter number 0 to 100: ")
print("You entered:", in1)
if int(in1) > 10:
    print("You entered number more than 10")
else:
    print("You entered number less or equal to 10")

# loops - циклы - набор действий
# while - цикл "до тех пор, пока"
# while fact:
#     блок действий

guess = "10"
enter = None
while enter != guess:
    enter = input("Please enter 10: ")
else:
    print("This is right answer")

# for loops - цикл for
# for iter in object:
#     исполнительный блок
    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list1)):
    list1[i] = list1[i] + 100
    list1[i] += 100
    print("Element", i, "is equal to ", list1[i])
    
for i in list1:
    i += 100
    print("Element is:", i)

list2 = ["Sergei", "Boris", "Fedor", 11, 10, 7, 3, 5]
list3 = [i for i in list2 if i in list1]
print(list3)

# keywords for loops - break, continue, pass
# break - принудительный выход из цикла
# continue - возврат на начало цикла
# pass - ничего не делать, роль заглушки

for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            break
        print(i, j)
print(".................. ")
for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            continue
        print(i, j)
print(" ")
for i in range(5):
    for j in range(5):
        if i == 2 or j == 2:
            pass
        print(i, j)
