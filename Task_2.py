# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Задайте размерность списка: '))
lst = [int(input(f'Введите {i} элемент списка: '))for i in range(n)]
if n % 2:
    n1 = n  // 2 + 1
else:
    n1 = n // 2
print('Произведение пар чисел списка равно: ')
lstNew = []
for i in range(n1):
    lstNew.append(lst[i] * lst[n - 1])
    n = n - 1 
print(lstNew)
