class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(20, 50)
b = Complex(30, 40)
c = a + b
d = a - b
print(f"A + B = {c}")
print(f"A - B = {d}")