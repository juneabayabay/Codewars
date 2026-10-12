class Student:
    @staticmethod
    def has_passed(score):
        return score >= 75

print(Student.has_passed(85))
print(Student.has_passed(60))
