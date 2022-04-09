class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Best', 'Student', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']

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
ineffectual_reviewer.rate_hw(best_student, 'Git', 10)
ineffectual_reviewer.rate_hw(worst_student, 'Git', 10)

best_student.rate_hw(cool_lecturer, 'Python', 8)
worst_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(ineffectual_lecturer, 'Git', 5)
best_student.rate_hw(ineffectual_lecturer, 'Python', 5)  # ошибка
worst_student.rate_hw(ineffectual_lecturer, 'Git', 8)

print(best_student.grades)
print(worst_student.grades)
print(cool_lecturer.grades)
print(ineffectual_lecturer.grades)