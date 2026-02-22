class Matrix:
    def __init__(self, rows, cols, mat=None):
        self.rows = rows
        self.cols = cols
        if mat is None:
            self.mat = [[0]*cols for _ in range(rows)]
        else:
            self.mat = mat

    def read_matrix(self):
        print("Enter matrix elements row by row:")
        for i in range(self.rows):
            row = list(map(int, input().split()))
            self.mat[i] = row

    def __add__(self, other):
        result = [
            [self.mat[i][j] + other.mat[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        result = [
            [self.mat[i][j] - other.mat[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        result = [
            [sum(self.mat[i][k] * other.mat[k][j] for k in range(self.cols))
             for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, other.cols, result)

    def display(self):
        for row in self.mat:
            print(row)

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("\nMatrix A")
A = Matrix(r, c)
A.read_matrix()

print("\nMatrix B")
B = Matrix(r, c)
B.read_matrix()

print("\nA + B =")
(A + B).display()

print("\nA - B =")
(A - B).display()

print("\nA * B =")
(A * B).display()
