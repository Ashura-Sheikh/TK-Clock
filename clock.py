import time
from tkinter import *

# Creating UI
root = Tk()

root.title("Ashura-Clock")

root.geometry("600x600")

root.config(bg="Black")

# Functions
def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
# If statements
    if int(h) > 12 and int(m) > 0:
            label_noon.config(text="PM")

    if int(h)>12:
        h = str((int(h)-12))


    label_hr.config(text=h)
    label_mn.config(text=m)
    label_sc.config(text=s)

    label_hr.after(200, clock)



# Label for Hours
label_hr = Label(root, text="12", font=("times new roman",40, "bold"), fg="white", bg="Green")
label_hr.place(x=100, y=50, width=80, height=60)

label_hr2 = Label(root, text="Hours", font=("times new roman",20, "bold"), fg="white", bg="Green")
label_hr2.place(x=100, y=120, width=80, height=40)

# Label for Minutes
label_mn = Label(root, text="12", font=("times new roman",40, "bold"), fg="white", bg="Green")
label_mn.place(x=200, y=50, width=80, height=60)

label_mn2 = Label(root, text="Minute", font=("times new roman",20, "bold"), fg="white", bg="Green")
label_mn2.place(x=200, y=120, width=80, height=40)

# Label for Seconds
label_sc = Label(root, text="12", font=("times new roman",40, "bold"), fg="white", bg="Red")
label_sc.place(x=300, y=50, width=80, height=60)

label_sc2 = Label(root, text="Sec", font=("times new roman",20, "bold"), fg="white", bg="Red")
label_sc2.place(x=300, y=120, width=80, height=40)

# Label For AM = PM
label_noon = Label(root, text="AM", font=("times new roman",25, "bold"), fg="white", bg="Red")
label_noon.place(x=400, y=50, width=80, height=60)

label_noon2 = Label(root, text="Noon", font=("times new roman",20, "bold"), fg="white", bg="Red")
label_noon2.place(x=400, y=120, width=80, height=40)

# calling the function in loop
clock()
root.mainloop()
