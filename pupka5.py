from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
   Student('Алексей', '13', 4.3, 'Рубцовск'),
   Student('Полина', '21', 5, 'Горняк'),
   Student('Дмитрий', '17', 2.9, 'Томск'),
   Student('Денис', '18', 3, 'Новосибирск'),
   Student('Дарья', '17', 4.5, 'Чулым'),
   Student('Алина', '18', 3.2, 'Краснодар'),
   Student('Кирилл', '16', 3.7, 'Омск')
)
def gs(students):
   tg = 0

   for student in students:
       tg += student.grade
   a = tg / len(students)

   g = [student.name for student in students if student.grade >= a]
   print('Ученики ', ', '.join(g), ' в этом семестре хорошо учатся!')

gs(students)