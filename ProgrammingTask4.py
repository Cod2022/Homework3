# Напишите программу, которая будет преобразовывать десятичное число в двоичное

a = int(input('Введите число для преобразования: '))

def decimal_to_binary_number (a):
    result = ""
    while a > 0:
        result = str(a % 2) + result
        a = a // 2
    return result

binary_number = decimal_to_binary_number(a)
print(f'результат преобразования: {binary_number}')