def gcd(a, b):
       while b != 0:
               a, b = b, a % b
       return a

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
print("GCD =", gcd(A, B))


