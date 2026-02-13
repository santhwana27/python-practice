class Rectangle:
    def __init__(self):
        self.length = float(input("Enter length: "))
        self.width = float(input("Enter width: "))

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



rect = Rectangle()

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
