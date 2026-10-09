class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        print(self.color)

class Circle(Shape):
    def __init__(self, color, radius):
        
        super().__init__(color) 
      
        self.radius = radius
      
