# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

n = int(input("Введите размер списка: "))
list1 = list(range(1, n+1))
print(f'Исходный список: {list1}')

count = 0
sum = 0

print('Элементы на нечётных позициях: ')

for i in list1:
    if count % 2 != 0:
        sum = sum + i
        print(i)
        count += 1
    else:
        count += 1

print(f'Сумма элементов на нечётных позициях: {sum}')
        