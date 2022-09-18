import pyqrcode
from tkinter import *
from tkinter import messagebox
import png

def generateQR():
    inputstr=entertextfield.get()
    scale=enterscalefield.get()
    if len(scale):
        try:
            scale=int(scale)
        except:
            messagebox.showerror("error","scale should be integer value")
    else:
        scale=5
    if len(inputstr):
        qrcode=pyqrcode.create(inputstr)
        savepath=""+inputstr+"_"+str(scale)
        qrcode.png(savepath+".png",scale=scale)
        messagebox.showinfo('success','qrcode is at:'+savepath)
    else:
        messagebox.showerror('Error','Text field is Empty')

def clearall():
    entertextfield.delete(0,END)
    entertextfield.focus_set()

tk=Tk()
#tk.configure(background='whight')
tk.geometry('400x200')
tk.title('QR code generator')
entertextlabel=Label(tk,text='Enter link:',fg='black',bg='grey')
entertextlabel.grid(row=2,column=1,sticky='E',padx='10',pady='10')
enterscalelabel=Label(tk,text='Scale:',fg='black',bg='grey')
enterscalelabel.grid(row=3,column=1,padx='10',pady='10')
entertextfield=Entry(tk)
entertextfield.grid(row=2,column=2,sticky='E',ipadx='60',pady='10')
enterscalefield=Entry(tk)
enterscalefield.grid(row=3,column=2,pady="10")
generatebtn=Button(tk,text="generate",fg='black',command=generateQR)
generatebtn.grid(row=4,column=2)
clearbtn=Button(tk,text='clear',fg='black',command=clearall)
clearbtn.grid(row=5,column=2,pady='5')

tk.mainloop()