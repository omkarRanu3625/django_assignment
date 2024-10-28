# Custom Class
#Rectangle Class

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    # Implementing the __iter__ method 
    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


rect = Rectangle(10, 5)

# Iterate over the Rectangle instance
for dimension in rect:
    print(dimension)
