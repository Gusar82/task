class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _middle_grade(self):
        sum_element = 0
        amount_element = 0
        for value in self.grades.values():
            sum_element += sum(value)
            amount_element += len(value)
        return round(sum_element/amount_element, 2)

    def __str__(self):
        text = f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашнее здания: {self._middle_grade()}\n"\
               f"Курсы в процессе изучения: { ', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self._middle_grade() < other._middle_grade()

    def __eq__(self, other):
        if not isinstance(other,Student):
            return
        return self._middle_grade() == other._middle_grade()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        text = f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"
        return text


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _middle_grade(self):
        sum_element = 0
        amount_element = 0
        for value in self.grades.values():
            sum_element += sum(value)
            amount_element += len(value)
        return round(sum_element / amount_element, 2)

    def __str__(self):
        text = super().__str__() + f"\nСредняя оценка за лекции: {self._middle_grade()}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._middle_grade() < other._middle_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self._middle_grade() == other._middle_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def middle_grade(persons, course):
    """Для подсчета средней оценки за лекции/домашние задания"""
    sum_element = 0
    amount_element = 0
    for person in persons:
        if course in person.grades:
            sum_element += sum(person.grades[course])
            amount_element += len(person.grades[course])
    if amount_element != 0:
        return round(sum_element/amount_element, 2)


best_student = Student('Best', 'Student', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в програмирование']

worst_student = Student("Worst", 'Student', 'female')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']

cool_reviewer = Reviewer('Cool', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

ineffectual_reviewer = Reviewer('Ineff', 'Reviewer')
ineffectual_reviewer.courses_attached += ['Git']

cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached += ['Python']

ineffectual_lecturer = Lecturer('Ineff', 'Lecturer')
ineffectual_lecturer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(worst_student, 'Python', 5)
cool_reviewer.rate_hw(worst_student, 'Git', 5)  # ошибка

ineffectual_reviewer.rate_hw(best_student, 'Git', 8)
ineffectual_reviewer.rate_hw(worst_student, 'Git', 10)

best_student.rate_hw(cool_lecturer, 'Python', 8)
worst_student.rate_hw(cool_lecturer, 'Python', 10)

best_student.rate_hw(ineffectual_lecturer, 'Git', 8)
best_student.rate_hw(ineffectual_lecturer, 'Python', 5)  # ошибка

worst_student.rate_hw(ineffectual_lecturer, 'Git', 10)

print(best_student)
print(best_student.grades)
print("----------------------")
print(worst_student)
print(worst_student.grades)
print("----------------------")
print(f"Best < Worst - {best_student < worst_student}")
print(f"Best > Worst - {best_student > worst_student}")
print(f"Best = Worst - {best_student == worst_student}")
print(f"Средняя оценка по курсу Git - {middle_grade([best_student,worst_student],'Git')}")
print(f"Средняя оценка по курсу Python - {middle_grade([best_student,worst_student],'Python')}")
print(f"Средняя оценка по курсу Введение - {middle_grade([best_student,worst_student],'Введение')}")
print("-----------------------")
print(cool_lecturer)
print(cool_lecturer.grades)
print('----------------------')
print(ineffectual_lecturer)
print(ineffectual_lecturer.grades)
print("''''''''''''''''''''''")
print(f"Cool < Ineff - {cool_lecturer < ineffectual_lecturer}")
print(f"Cool > Ineff - {cool_lecturer > ineffectual_lecturer}")
print(f"Cool = Ineff - {cool_lecturer == ineffectual_lecturer}")
print(f"Cool < Worst - {cool_lecturer < worst_student}")  # None
print(f"Средняя оценка по курсу Git - {middle_grade([cool_lecturer,ineffectual_lecturer],'Git')}")
print(f"Средняя оценка по курсу Python - {middle_grade([cool_lecturer,ineffectual_lecturer],'Python')}")
print("''''''''''''''''''''''")
print(cool_reviewer)
print('----------------------')
print(ineffectual_reviewer)