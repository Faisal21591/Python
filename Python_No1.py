from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
win=Tk()
win.title("Faisal Riaz")
win.iconbitmap(r"H:\Python\extra work with photos\heart_black.ico")
width=1200
height=700
sys_width=win.winfo_screenwidth()
sys_height=win.winfo_screenheight()
c_x=int(sys_width/2-width/2)
c_y=int(sys_height/2-height/2)
win.geometry("{}x{}+{}+{}".format(width, height, c_x, c_y))
win.configure(background="light blue")
Lf1=LabelFrame(win,text="Hello World",font=("Arial",14,"bold"),width=800,height=600,labelanchor=N,
               bg="green",fg="white")
Lf1.place(x=0,y=0)
nb=ttk.Notebook(Lf1,width=200,height=200)
nb.place(x=300,y=100)

f1=Frame(nb,bg="#b4cf66")
f2=Frame(nb,bg="#fffc5c")
f3=Frame(nb,bg="#ff5a33")
photo2=PhotoImage(file=r"H:\Python\extra work with photos\cricket.png")
photo2=photo2.subsample(5)
l1=Label(f1,text="  Cricket  ",font=("Arial",14,"bold"),bg="#ff5a33",image=photo2,compound=TOP)
l1.place(x=35,y=30)

photo1=PhotoImage(file=r"H:\Python\extra work with photos\family.png")
photo1=photo1.subsample(9)
l2=Label(f2,text="Family",font=("Arial",14,"bold"),bg="#ff5a33",image=photo1,compound=TOP)
l2.place(x=10,y=30)

photo=PhotoImage(file=r"H:\Python\extra work with photos\charry.png")
photo=photo.subsample(2,2)
l3=Label(f3,text="Cherry",font=("Arial",14,"bold"),bg="#ff5a33",image=photo,compound=TOP)
l3.place(x=30,y=30)
nb.add(f1,text="   Cricket   ")
nb.add(f2,text="    Family   ")
nb.add(f3,text="    Cherry   ")
def on_tab_hover(event):
    x, y = event.x, event.y
    tab_index = nb.index(f"@{x},{y}") if nb.identify(x, y) == "label" else None
    if tab_index is not None:
        nb.select(tab_index)

# Bind mouse movement
nb.bind("<Motion>", on_tab_hover)



win.mainloop()