import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Боря',
    'Дмитрий', 'Борис', 'Елена', 'Боря'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutors_classes = (i for i in itertools.zip_longest(tutors, classes))
print(type(tutors_classes))
print(*tutors_classes)
