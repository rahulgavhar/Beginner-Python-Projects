# requirements: tkinter, base64
from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()
    if code.get().isdigit():
        pass
    else:
        messagebox.showerror("Error","Please enter only numbers")
        code.set("")
        return
    if password=="":
        messagebox.showerror("Please enter a Key")
    if len(code.get())>12:
        messagebox.showerror("Error:","Please enter only 12 digits")
        code.set("")
        return
    if password=="25032004":
        screen2=Toplevel(screen)
        screen2.title("Notello")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message=text1.get(1.0,END)
        decoded_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decoded_message)
        decrypt=base64_bytes.decode("ascii")
        
        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        
        text2.insert(END,decrypt)
    if password!="25032004":
        messagebox.showerror("Error","Wrong Key")
        code.set("")
        return
    print("")

def encrypt():
    password = code.get()
    if code.get().isdigit():
        pass
    else:
        messagebox.showerror("Error:","Please enter only numbers")
        code.set("")
        return
    if len(code.get())>12:
        messagebox.showerror("Error:","Please enter only 12 digits")
        code.set("")
        return
    else:
        pass
    if password=="":
       messagebox.showerror("Please enter a Key")
    
    if password=="25032004":
        screen1=Toplevel(screen)
        screen1.title("Notello")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3883")
        
        message=text1.get(1.0,END)
        encoded_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encoded_message)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3883").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        
        text2.insert(END,encrypt)
    if password!="25032004":
        messagebox.showerror("Error","Wrong Key")
        code.set("")
        return
def main_screen():
    global screen,code,text1
    screen=Tk()
    screen.geometry("375x370")
    
    #icon
    #use https://static.vecteezy.com/system/resources/previews/021/013/593/non_2x/key-lock-icon-on-transparent-background-free-png.png
    image_icon = PhotoImage(file="TestFiles/keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Notello")
    
    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    Label(text="Enter text for encryption or decryption:", fg="black",font=("Calibri", 12)).place(x=10,y=10)
    text1 = Text(font="Robote 10", bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=40,width=355,height=100)
    
    Label(text="Enter secret key (upto 12 digits):", fg="black",font=("Calibri", 12)).place(x=10,y=170)
    
    code=StringVar()
    Entry(textvariable=code,width=23,bd=0,font=("arial", 20),show="*").place(x=10,y=200)
    
    Button(text="ENCRYPT",width=23,height=2,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",width=23,height=2,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",width=50,height=2,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)
    
    screen.mainloop()
main_screen()
