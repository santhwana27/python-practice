from tkinter import *

def calculate(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if op == "sum":
            result.set(a + b)
        elif op == "diff":
            result.set(a - b)
        elif op == "prod":
            result.set(a * b)
        elif op == "div":
            result.set(a / b if b != 0 else "Error: Div by 0")
    except:
        result.set("Invalid Input")

root = Tk()
root.title("Simple Calculator")

entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry2 = Entry(root)
entry2.grid(row=1, column=1)

Label(root, text="Number 1").grid(row=0, column=0)
Label(root, text="Number 2").grid(row=1, column=0)
Label(root, text="Result").grid(row=2, column=0)

result = StringVar()
Entry(root, textvariable=result, state="readonly").grid(row=2, column=1)

Button(root, text="Sum", command=lambda: calculate("sum")).grid(row=3, column=0)
Button(root, text="Difference", command=lambda: calculate("diff")).grid(row=3, column=1)
Button(root, text="Product", command=lambda: calculate("prod")).grid(row=4, column=0)
Button(root, text="Quotient", command=lambda: calculate("div")).grid(row=4, column=1)

root.mainloop()
