from tkinter import *
import time
root = Tk()

root.title("Heure")
root.geometry("1920x1080+0+0")
root.config(bg="black")

def recupereHeure():
    h = (time.strftime("%H"))
    m = (time.strftime("%M"))
    s = (time.strftime("%S"))

    print(h, m, s)

    lbl_heure.config(text=h)
    lbl_minute.config(text=m)
    lbl_seconde.config(text=s)


    lbl_heure.after(200, recupereHeure)


heureactuel = (0, 0, 0,)

#heure
lbl_heure= Label(root, text="12", font=("times new roman", 50, "bold"), bg="green")
lbl_heure.place(x=200, y=300, width=200, height=80)

heure = Label(root, text="Heure", font=("times new roman", 20, "bold"), bg="green")
heure.place(x=200, y=450, width=200, height=30)



#minute
lbl_minute= Label(root, text="30", font=("times new roman", 50, "bold"), bg="yellow")
lbl_minute.place(x=500, y=300, width=200, height=80)

minute = Label(root, text="Minute", font=("times new roman", 20, "bold"), bg="yellow")
minute.place(x=500, y=450, width=200, height=30)


#seconde
lbl_seconde= Label(root, text="50", font=("times new roman", 50, "bold"), bg="red")
lbl_seconde.place(x=800, y=300, width=200, height=80)

seconde = Label(root, text="Seconde", font=("times new roman", 20, "bold"), bg="red")
seconde.place(x=799, y=450, width=200, height=30)


recupereHeure()

root.mainloop()