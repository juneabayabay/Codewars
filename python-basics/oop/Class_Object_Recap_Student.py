class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create three student objects
student1 = Student("Alice", 18)
student2 = Student("Bob", 20)
student3 = Student("Charlie", 19)

# Display each student's information
student1.display_info()
print()

student2.display_info()
print()

student3.display_info()
