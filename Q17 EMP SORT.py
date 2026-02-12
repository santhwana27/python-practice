emp = ((1, 'John', 50000), (3, 'Alice', 60000), (2, 'Bob', 40000))

print("By ID Asc:", sorted(emp))
print("By ID Desc:", sorted(emp, reverse=True))
print("By Name Asc:", sorted(emp, key=lambda x: x[1]))
print("By Name Desc:", sorted(emp, key=lambda x: x[1], reverse=True))
print("By Salary Asc:", sorted(emp, key=lambda x: x[2]))
print("By Salary Desc:", sorted(emp, key=lambda x: x[2], reverse=True))