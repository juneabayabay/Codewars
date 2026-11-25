class Father:
    def father_skill(self):
        print("Father: Programming")

class Mother:
    def mother_skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child: Gaming")

child = Child()
child.father_skill()
child.mother_skill()
child.child_skill()

# My understanding of multiple inheritance is that it allows a child class to inherit from multiple parent classes.
# we created a parent class called Father and a parent class called Mother and a child class called Child.
# then we can use the multiple inheritance to inherit the methods of the parent classes.
# and we can also use the multiple inheritance to call the methods of the parent classes.
