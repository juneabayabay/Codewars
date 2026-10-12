class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


student = Student.from_string("Arjune,21")

print(f"Name: {student.name}")
print(f"Age: {student.age}")
