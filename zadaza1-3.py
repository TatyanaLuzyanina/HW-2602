class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lectures, course, grade):
        if isinstance(lectures, Lectures) and course in self.courses_in_progress and course in lectures.courses_attached:
            if course in lectures.grades:
                lectures.grades[course] += [grade]
            else:
                lectures.grades[course] = [grade]
        else:
            return 'Ошибка'
    def av_rate(self, course):
        if course in self.grades.keys():
            return sum(self.grades[course]) / len(self.grades[course])
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Ср. оценка: {round(sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0]), 1)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
                )
    def __lt__(self, other):
        n = 0
        for i in self.grades.values():
            n += sum(i)
        m = 0
        for i in self.grades.values():
            m += len(i)
        t = 0
        for i in other.grades.values():
            t += sum(i)
        r = 0
        for i in other.grades.values():
            r += len(i)
        return n / m > t / r

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectures(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def av_rate(self, course):
        if course in self.grades.keys():
            Av_rate_lect = sum(self.grades[course]) / len(self.grades[course])
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Ср. оценка: {round(sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0]), 1)}\n")

    def __lt__(self, other):
        n = 0
        for i in self.grades.values():
            n += sum(i)
        m = 0
        for i in self.grades.values():
            m += len(i)
        t = 0
        for i in other.grades.values():
            t += sum(i)
        r = 0
        for i in other.grades.values():
            r += len(i)
        return n / m > t / r

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")
lecture1 = Lectures('Oleg', 'Bulygin')
lecture1.courses_attached += ['Python']
lecture2 = Lectures('Иван', 'Иванов')
lecture2.courses_attached += ['Математика']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Математика', 'Python']
best_student1 = Student('Костя', 'Петров', 'муж')
best_student1.courses_in_progress += ['Математика', 'Python']

best_student.rate_hw(lecture1, 'Python', 10)
best_student1.rate_hw(lecture1, 'Python', 10)

best_student.rate_hw(lecture1, 'Python', 10)
best_student1.rate_hw(lecture1, 'Python', 10)

best_student.rate_hw(lecture1, 'Python', 10)
best_student1.rate_hw(lecture1, 'Python', 10)

best_student.rate_hw(lecture2, 'Математика', 5)
best_student1.rate_hw(lecture2, 'Математика', 6)

best_student.rate_hw(lecture2, 'Математика', 5)
best_student1.rate_hw(lecture2, 'Математика', 8)

best_student.rate_hw(lecture2, 'Математика', 5)
best_student1.rate_hw(lecture2, 'Математика', 9)

lecture1.av_rate("Python")
lecture2.av_rate("Математика")

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Петя', 'Петров')
reviewer2.courses_attached += ['Математика']

reviewer1.rate_hw(best_student, 'Python', 0)
reviewer1.rate_hw(best_student1, 'Python', 10)

reviewer1.rate_hw(best_student, 'Python', 5)
reviewer1.rate_hw(best_student1, 'Python', 9)

reviewer1.rate_hw(best_student, 'Python', 3)
reviewer1.rate_hw(best_student1, 'Python', 8)

reviewer2.rate_hw(best_student, 'Математика', 4)
reviewer2.rate_hw(best_student1, 'Математика', 10)

reviewer2.rate_hw(best_student, 'Математика', 5)
reviewer2.rate_hw(best_student1, 'Математика', 9)

reviewer2.rate_hw(best_student, 'Математика', 3)
reviewer2.rate_hw(best_student1, 'Математика', 5)

best_student.av_rate("Python")
best_student1.av_rate("Python")

best_student.add_courses("Основы программирования")
best_student1.add_courses("Python")

print(best_student)
print(lecture1)
print(reviewer1)

#Задача 3.2:
print(best_student.__lt__(best_student1))
print(lecture1.__lt__(lecture2))

