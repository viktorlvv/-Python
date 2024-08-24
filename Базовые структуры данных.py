grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортируем студентов для соответствия с оценками
sorted_students = sorted(students)

# Создаем словарь для хранения средних баллов
average_grades = {}

# Вычисляем средний балл для каждого ученика
for i, student in enumerate(sorted_students):
    average = sum(grades[i]) / len(grades[i])  # Средний балл
    average_grades[student] = average

# Выводим результаты
print(average_grades)