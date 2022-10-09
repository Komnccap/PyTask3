# Задача №1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def task1():
    nums = [10, 5, 15, 20, 11]
    counter = 0
    current_nums = 0
    while counter < 5:
            current_nums += nums[counter]
            counter += 2
    print(nums)
    print('Сумма чисел на нечётных позиция равно: ')
    print (current_nums)
task1()    
# Задача №2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def task2():
    print('Введите Значение N')
    nums = [2, 3, 4, 5, 6]
    counter = 0
    first_element = nums[0]
    end_element = nums[4]
    while counter < 5:
        counter += 1
        if counter <= 3:
            print(first_element * end_element)
            first_element += 1
            end_element -= 1
    print(nums)
task2()
# Задача №3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def task3():
    float_list = [1.1, 1.2, 3.1, 5, 10.01]
    counter = 0
    current_nums = 0.0
    min_value = float_list[0]
    max_value = float_list[0]
    while counter < 4:
        counter += 1
        current_nums = float_list[counter]
        if current_nums % 1 > max_value % 1:
            max_value = current_nums % 1
        elif max_value % 1 > current_nums % 1:
            min_value = current_nums % 1
    print("Разница между максимальным и минимальным значением дробной части ровна: ")
    print(round(max_value - min_value, 2))
task3()
# Задача №4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def task4():
    num = 8
    ost = ''
    while num > 0:
        ost = str(num % 2) + ost
        num = num // 2
    print (ost)
task4()
