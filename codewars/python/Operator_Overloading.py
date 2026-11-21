class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be of type Vector")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls v1.__add__(v2)

print(v3)  # Output: Vector(6, 8)
