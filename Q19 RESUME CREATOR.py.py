from tkinter import *

def save_resume():
    name = name_entry.get()
    age = age_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    quali = quali_entry.get()

    content = (
        f"Resume\n"
        f"--------\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Date of Birth: {dob}\n"
        f"Gender: {gender}\n"
        f"Qualifications: {quali}\n"
    )

    # saves as a simple .doc text file
    with open("Resume.doc", "w") as f:
        f.write(content)

    status_label.config(text="Resume saved as resume.doc")

root = Tk()
root.title("Resume Maker")

Label(root, text="Name").grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Age").grid(row=1, column=0)
age_entry = Entry(root)
age_entry.grid(row=1, column=1)

Label(root, text="DOB").grid(row=2, column=0)
dob_entry = Entry(root)
dob_entry.grid(row=2, column=1)

Label(root, text="Gender").grid(row=3, column=0)
gender_var = StringVar(value="Male")
Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(row=3, column=1)
Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(row=3, column=2)

Label(root, text="Qualifications").grid(row=4, column=0)
quali_entry = Entry(root)
quali_entry.grid(row=4, column=1)

Button(root, text="Save Resume", command=save_resume).grid(row=5, column=1)
status_label = Label(root, text="")
status_label.grid(row=6, column=1)

root.mainloop()
