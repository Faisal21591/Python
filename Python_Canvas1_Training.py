from tkinter import *
from tkinter import ttk
window=Tk()
window.title("Canvas")

# Set window icon
icon = PhotoImage(file=r"H:\Python\extra work with photos\Apple_1.png")
window.iconphoto(True, icon)
window.config(background="black")

width = 1300
height = 600
sys_width = window.winfo_screenwidth()
sys_height = window.winfo_screenheight()

# ✅ Corrected centering logic
c_x = int((sys_width / 2) - (width / 2))
c_y = int((sys_height / 2) - (height / 2))
window.geometry(f"{width}x{height}+{c_x}+{c_y}")
window.resizable(False, False)
window.configure(background="light blue")
canvas = Canvas(window, width=500, height=500,bg="blue")
blueline=canvas.create_line(0,0,500,500, fill="light blue",width=3)
redline=canvas.create_line(0,500,500,0, fill="red",width=3)
rectangle_1=canvas.create_rectangle(50,50,250,150,fill="orange",width=3)
points=[250,0,500,500,0,500]
polygon_1=canvas.create_polygon(points,fill="purple",width=3,outline="white")
arc_1=canvas.create_arc(0,0,500,500,fill="red",width=3,style=PIESLICE,extent=180,start=270)
                     #(x,y,height and width),#style = ARC or CHORD,start=0 dgree or 90 or 180 etc,extend=180 degree
canvas_2=Canvas(window,width=500,height=500,bg="light green")

canvas.place(x=10,y=50)
canvas_2.place(x=550,y=50)
arc_2=canvas_2.create_arc(0,0,500,500,fill="red",width=3,style=PIESLICE,extent=180,start=0)
arc_3=canvas_2.create_arc(0,0,500,500,fill="white",width=3,style=PIESLICE,extent=180,start=180)
oval_1=canvas_2.create_oval(150,150,350,350,fill="light yellow",width=3)
window.mainloop()