from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

#Defining Class and constructor of the Program
class Draw():
    def __init__(self,root):
        # Defining title and Size of the Tkinter Window GUI
        self.root = root
        self.root.title("Copy Assignment Painter")
        self.root.configure(background = "white")

        # variables for pointer and Eraser
        self.pointer = "black"
        self.erase = "white"

        # Configure the aligment , font size and color of the text
        text=Text(root)

        # Insert a Text
        text.insert("1.0", "Drawing Application in Python")

        # Add the tag for following given text
        text.tag_add("tag_name", "1.0", "end")
        text.pack()