from tkinter import *

root = Tk()
root.title("Image on Canvas")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

img = PhotoImage(file="xyz.jpg")  

canvas.create_image(200, 150, image=img)

root.mainloop()