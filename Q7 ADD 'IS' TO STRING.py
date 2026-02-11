def add_is(s):
       if s.startswith("is"):
           return s
       return "is" + s
s= input("Enter a string:  ")
print(add_is(s))
