class Person:
    def introduce(self):
        print("I am person")

    def role(self):
        print("I have a role in the school")


class Teacher(Person):
    def introduce(self):
        print("I am a teacher")

    def role(self):
        print("I teach students")


class Student(Person):
    def introduce(self):
        print("I am student")

    def role(self):
        print("I study different subjects")


person = Person()
teacher = Teacher()
student = Student()

person.introduce()
person.role()

teacher.introduce()
teacher.role()

student.introduce()
student.role()
