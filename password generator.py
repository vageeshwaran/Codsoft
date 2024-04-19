from tkinter import *
import random
import string

root = Tk()
root.title("PASSWORD GENERATOR")

def generate_password():
    length = int(enter_length.get())
    characters = string.ascii_letters +  "@#$&?+-"+ string.digits
    password = ''.join(random.sample(characters, length))
    output.config(text="Generated Password: " + password)

length_label = Label(root, text="Enter the length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

enter_length = Entry(root, width=20)
enter_length.grid(row=0, column=1, padx=5, pady=5)

generate_button = Button(root, text="Generate Password", padx=5, pady=5, background="light green", command=generate_password)
generate_button.grid(row=1, column=1, padx=5, pady=5)

output = Label(root, text="")
output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()