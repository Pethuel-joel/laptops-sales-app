import tkinter as tk
from tkinter import messagebox


def submit():
    name = name_entry.get()
    phone = phone_entry.get()
    make = make_var.get()
    model = model_var.get()

    if make == "mac":
        if model == "macbook air":
            messagebox.showinfo("Laptop Sales Tech", "Mr/Mrs "+name+", you have selected macbook air, the cost is $500")
        elif model == "macbook pro":
            messagebox.showinfo("Laptop Sales Tech", "Mr/Mrs "+name+", you have selected macbook pro, the cost is $700")
        elif model == "macbook air m1":
            messagebox.showinfo("Laptop Sales Tech", "Mr/Mrs "+name+", you have selected macbook air, the cost is $6500")
    elif make == "HP":
        if model == "envy":
            messagebox.showinfo("Laptop Sales Tech", "Mr/Mrs "+name+", you have selected Envy, the cost is $500")
        elif model == "elitebook":
