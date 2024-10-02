grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
# список по алфавиту

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# словарь с нефиксированными значениями

sorted_students = sorted(students)
# сортируем по алфавиту
print(sorted_students)
# вывожим для проверки

for i, student in enumerate(sorted_students): # создаем цикл с нулевого i, создавая переменную student,
    # просим пронумеровать с 1
    student_grades = grades[i]
    # пройтиись по list с нулевого i
    average_grade = sum(student_grades) / len(student_grades)
    # создаем новую переменную и вычесляем в ней сумму переменной / на колличество символов в переменной
    print({student},":", {average_grade})
    # print(f"{student}: {average_grade:.1f}")

    # выводим подставляя float в str
    # берем student поочередно
    # выводя внутри цикла поочередно с помощью i, операцию sum/len внутри переменной  average_grade






