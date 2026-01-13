class Person:
    def __init__(self, name):
        self._name = name # encapsulated (protected)


    def introduce(self):
        return f"Hello, I am {self._name}"




class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self): # polymorphism
        return f"Hello, I am {self._name}, student ID: {self.student_id}"




def run():
    person = Person("John")
    student = Student("Anna", "S123")


    people = [person, student]

    for p in people:
        print(p.introduce())