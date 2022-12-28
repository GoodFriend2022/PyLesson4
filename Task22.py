# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random

def CreateArray(length):
    array = []
    for i in range(length):
        array.append(random.randint(0, 15))
    return array

n = int(input('Введите кол-во элементов первого набора > '))
m = int(input('Введите кол-во элементов второго набора > '))
nArray = CreateArray(n)
mArray = CreateArray(m)
print(nArray)
print(mArray)
firstSet = set(nArray)
secondSet = set(mArray)
numbers = firstSet.intersection(secondSet)
if len(numbers) != 0:
    print(numbers)
else: 
    print('В Ваших наборах нет одинаковых элементов')



