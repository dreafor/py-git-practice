class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def get_info(self):
        return f"Студент: {self.name}, группа: {self.group}, средний балл: {self.average_grade}"
