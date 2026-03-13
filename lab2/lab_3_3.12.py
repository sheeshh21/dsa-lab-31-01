import sys
import random

# 1. Считывание массива
if len(sys.argv) < 11:
    print("Ошибка: нужно ввести 10 чисел")
    sys.exit()

A = []
for i in range(1, 11):
    A.append(int(sys.argv[i]))

print("Массив A:", A)

# 2. Нахождение наименьшего элемента
min_nechet = None
for num in A:
    if num % 2 != 0:  # нечетное
        if min_nechet is None or num < min_nechet:
            min_nechet = num

if min_nechet is None:
    print("Нет нечетных элементов")
else:
    print("Наименьший нечетный элемент:", min_nechet)

# 3. Заполнение массива B
B = []
for i in range(10):
    B.append(random.randint(1, 100))

print("Массив B (до замены):", B)

# 4. Обмен местами A и B
A, B = B, A

# 5. Результат
print("Массив A (после замены):", A)
print("Массив B (после замены):", B)