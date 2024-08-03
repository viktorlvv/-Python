first = int(input('Введите первое число: '))
print("Первое число: ", first)
second = int(input('Введите второе число: '))
print("Второе число: ", second)
third = int(input('Введите третье число: '))
print("Третье число: ", third)
if first == second and second == third:
    print("Введённые числа одинаковы: 3")
elif first != second and first != third and second != third:
    print("Одинаковых чисел нет: 0")
else:
    print("Есть два одинаковых числа: 2")




