# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list1 = [2, 10, 11, 25, 3]
list2 = []
count = 5

for i in range(len(list1)):
    while i < len(list1) / 2 and count > len(list1) / 2:
        count = count -1
        m = list1[i] * list1[count]
        list2.append(m)
        i = i + 1
        

print(f'Исходный список: {list1}')
print(f'Произведения пар чисел списка: {list2}')
