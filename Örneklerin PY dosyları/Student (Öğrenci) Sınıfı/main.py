class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# Kullanım
student1 = Student("Alice", 1234)
student1.add_grade(90)
student1.add_grade(85)
student1.add_grade(88)

print(student1.get_average_grade())  # 87.67
