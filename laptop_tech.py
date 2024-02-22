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
  messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected HP Elitebook, the cost is $800")
        elif model == "pavilion":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected pavilion, the cost is $800")
    elif make == "Dell":
        if model == "xps17":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell xps17, the cost is $500")
        elif model == "inspion":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell inspion, the cost is $6600")
        elif model == "latitude":
            messagebox.showinfo("Laptop Sales Tech",
                                "Mr/Mrs " + name + ", you have selected Dell latitude, the cost is $800")
