import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import Label
from tkinter import Button

root = tk.Tk()
root.title("Colour App")
root.geometry("500x500")
root.config(background = "#6A0DAD")
def fileBrowse():
    fileName = askopenfilename(initialdir='/home/{}', title="Select wallpaper")
    label_file_explorer.configure(text="File Opened: "+fileName)
label_file_explorer = Label(root, 
                            text = "Colour App",
                            width = 100, height = 4, 
                            bg = "#DDA0DD")
label_file_explorer.grid(column = 1, row = 1)

button_explore = Button(root, 
                        text = "Browse Files",
                        command = fileBrowse)
button_explore.grid(column = 1, row = 2)

root.mainloop()
