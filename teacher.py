class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def get_info(self):
        return f"Преподаватель: {self.name}, дисциплина: {self.subject}, стаж: {self.experience} лет"
