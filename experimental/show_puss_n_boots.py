__author__ = 'timtiptoes'
#Taken from https://books.google.com/books?id=JnR9hQA3SncC&pg=PA414&dq=python+tk+images&hl=en&sa=X&ved=0CB0Q6AEwAGoVChMIjLSZsd-wyAIVwjeICh1fqQKR#v=onepage&q=python%20tk%20images&f=false
import os
import Tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()
img = Image.open("/Users/JenLevine/Downloads/mcaw.JPG")
tk_img = ImageTk.PhotoImage(img)
canvas.create_image(500, 500, image=tk_img)
root.mainloop()