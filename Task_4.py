# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def tentotwo(n):

# if n == 0:
# return ''
# return tentotwo(n//2) + str(n % 2)

# num = int(input('Введите десятичное число '))
# print(tentotwo(num))

N = int(input('Введите число '))
s = ''
while N > 0:
    s = str(N % 2) + s
    N = N // 2
print(s)