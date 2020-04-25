import tkinter as tk
import glob
from PIL import Image, ImageTk
import os

def insertfiles():
    # lst.delete(0, tk.END)
    for filename in glob.glob("*.png"):
        lst.insert(tk.END, filename)

def delete_item(event):
    n = lst.curselection()
    os.remove(lst.get(n))
    lst.delete(n)


def get_window_size():
    if root.winfo_width() > 200 and root.winfo_height() >30:
        w = root.winfo_width() - 200
        h = root.winfo_height() - 30
    else:
        w = 200
        h = 30
    return w, h


def showimg(event):
    n = lst.curselection()
    filename = lst.get(n)
    im = Image.open(filename)
    im = im.resize((get_window_size()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    w, h = img.width(), img.height()
    canvas.image = img
    canvas.config(width=w, height=h)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    root.bind("<Configure>", lambda x: showimg(x))



root = tk.Tk()

root.geometry("800x600+300+50")
lst = tk.Listbox(root, width=20)
lst.pack(side="left", fill=tk.BOTH, expand=0)
lst.bind("<<ListboxSelect>>", showimg)
lst.bind("<Control-d>", delete_item)
insertfiles()
canvas = tk.Canvas(root)
canvas.pack()

root.mainloop()
