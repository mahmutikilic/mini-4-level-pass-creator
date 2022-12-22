import tkinter as tk
from tkinter import END, ttk,messagebox
import random as r

#password length choose
count = 8
def countplus():
    global count
    count += 1
    PasslengthLabel.config(text = f"{count}")
    if count >=10:
        buttonplus.place(x = 305, y = 50)
    elif count >= 100:
        buttonplus.place(x = 330, y = 50)
    return count

def countminus():
    global count
    count -= 1
    PasslengthLabel.config(text = f"{count}")
    return count

def returnPass(radivar,count):
    passString = "abcdefghijklmnoprstuvyzwx1234567890ABCDEFGHIJKLMNOPRSTUVYZWX.,!'^+%&/()=?-_"
    if radivar == 1:
        passresult = "".join(r.sample(passString[25:35],count))
        return str(passresult)

    elif radivar == 2:
        passresult = "".join(r.sample(passString[:35],count))
        return str(passresult)

    elif radivar == 3:
        passresult = "".join(r.sample(passString[:63],count))
        return str(passresult)

    elif radivar == 4:
        passresult = "".join(r.sample(passString[:76],count))
        return str(passresult)

def radiVarCheck():
    if radivar.get() == 1: # eklenmiş veya atanmış değeri çeker
        # createdPassLabel.configure(state = "Disabled")
        createdPassEntry.delete(0,END)
        createdPassEntry.insert(string = f"{returnPass(radivar.get(),count)}",index = 0)
    elif radivar.get() == 2:
        createdPassEntry.delete(0,END)
        createdPassEntry.insert(string = f"{returnPass(radivar.get(),count)}",index = 0)
    elif radivar.get() == 3:
        createdPassEntry.delete(0,END)
        createdPassEntry.insert(string = f"{returnPass(radivar.get(),count)}",index = 0)
    elif radivar.get() == 4:
        createdPassEntry.delete(0,END)
        createdPassEntry.insert(string = f"{returnPass(radivar.get(),count)}",index = 0)
    else:
        #createdPassText.config(text="Pass level is not selected! Please choose level.")
        #print("Error!, PassKey level is not selected!")
        message_box = messagebox.showerror(title="Error!",message="Complexity choose error!")

    # messagebox.showinfo
    # messagebox.askretrycancel
    # messagebox.asquestion
    # messagebox.askyesnocancel
window = tk.Tk() # pencere tanımlama
window.title("Randomize Password Creator")
window.geometry("300x200") #ilk yatay sonra dikey, x y 
window.minsize(375,220) # en fazla azalabileceği ölçüler, en fazla artailecek ölçüler için window.maxsize(400,300)
window.resizable(0,0) # büyüme ve küçülmeyi kapatma x ve y de
# window.state("normal") ilk açılışta nasıl olması gerektiği 
passLenghtnotify = messagebox.showinfo(title="Minimum password Length", message="Default password length is set to 8.")
metin1 = tk.Label(text = "| Pass Complexity | Pass Lenght |",font=("Helvetica", 18))
metin1.place(x=5, y=5)
rdb1= tk.Radiobutton(window,text = "Easy Password(123)", value = 1, variable = radivar)
rdb1.place(x= 20, y= 50)
rdb2= tk.Radiobutton(window,text = "Medium Password(gb12)", value = 2, variable = radivar)
rdb2.place(x= 20, y = 70)
rdb3= tk.Radiobutton(window,text = "Hard Password(Cd2,.)", value = 3, variable = radivar)
rdb3.place(x= 20, y = 90)
rdb4= tk.Radiobutton(window,text = "İmposible Password(?x4A)", value = 4, variable = radivar)
rdb4.place(x= 20, y = 110)
button=tk.Button(window, text = "Create Password", command=radiVarCheck, bg="gray", fg="white")
button.place(x=60, y = 150)
notiftext= tk.Label(window, text = "Click Button and Copy pass", fg="gray",font="bold 15")
notiftext.place(x= 10, y = 180)
createdPassEntry = tk.Entry(window, width =20)
createdPassEntry.insert(string = "Copy text...", index = 0) # buraya oluşturulan kod eklenecek** 
createdPassEntry.place(x = 170, y = 154)
buttonplus=tk.Button(window, text = " + ", command=countplus, bg="gray", fg="white")
buttonplus.place(x = 290, y = 50)
PasslengthLabel= tk.Label(window, text = count, fg="gray",font="bold 20")
PasslengthLabel.place(x= 265, y = 45)
buttonminus=tk.Button(window, text = " - ", command=countminus, bg="gray", fg="white")
buttonminus.place(x = 240, y = 50)

window.mainloop()
