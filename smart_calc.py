from tkinter import *
from tkinter import Button
from tkinter import messagebox       # to give an alert messege
import math

screen = Tk()  # to make a screen
screen.title("My Calculator")  # to give the title
screen.iconbitmap(r'calculator.ico')  # r stands for raw string whenever we want to give some location
screen.configure(bg="chocolate")  # for overall background color
# screen.geometry('380x500')  # to give the height and width but it can be changed
screen.maxsize(width=487, height=510)  # to keep the size fixed
screen.minsize(width=380, height=510)
screen.geometry('380x510')


def click(number):  # function used if any number is clicked
    global operator
    operator += str(number)  # the number will be stored in operator
    tex.set(operator)  # and the value of the operator will be set in entry1

def clear():                    #this function is called when clear(C) is called
    global operator
    operator=''
    tex.set(operator)

def equal():
    global operator
    try:
        result= eval(operator)  #eval is a built in module which will evaluate all the values present in the operator
        operator=str(result)    #conversion in string is important as eval takes string value
        tex.set(result)
    except:
        messagebox.showinfo('Notify','Try again,some thing is wrong',parent=screen)

def cmsin():
    global operator
    try:
        result=math.sin(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify', 'Try again,some thing is wrong', parent=screen)

def cmcos():
    global operator
    try:
        result=math.cos(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify', 'Try again,some thing is wrong', parent=screen)

def cmtan():
    global operator
    try:
        result=math.tan(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify', 'Try again,some thing is wrong', parent=screen)

def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify', 'Try again,some thing is wrong', parent=screen)

def cmlog():
    global operator
    try:
        result=math.log(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notify', 'Try again,some thing is wrong', parent=screen)


#####################################binding functions#########################3

def on_enter7(e):
    btn7.configure(bg="green")          #syntax for hover effect

def on_leave7(e):
    btn7.configure(bg="burlywood")

def on_enter8(e):
    btn8.configure(bg="green")          #syntax for hover effect

def on_leave8(e):
    btn8.configure(bg="burlywood")

def on_enter9(e):
    btn9.configure(bg="green")          #syntax for hover effect

def on_leave9(e):
    btn9.configure(bg="burlywood")

def on_enterplus(e):
    btnplus.configure(bg="green")          #syntax for hover effect

def on_leaveplus(e):
    btnplus.configure(bg="burlywood")

def on_enter4(e):
    btn4.configure(bg="green")          #syntax for hover effect

def on_leave4(e):
    btn4.configure(bg="burlywood")

def on_enter5(e):
    btn5.configure(bg="green")          #syntax for hover effect

def on_leave5(e):
    btn5.configure(bg="burlywood")

def on_enter6(e):
    btn6.configure(bg="green")          #syntax for hover effect

def on_leave6(e):
    btn6.configure(bg="burlywood")

def on_entersub(e):
    btnsub.configure(bg="green")          #syntax for hover effect

def on_leavesub(e):
    btnsub.configure(bg="burlywood")

def on_enter1(e):
    btn1.configure(bg="green")          #syntax for hover effect

def on_leave1(e):
    btn1.configure(bg="burlywood")

def on_enter2(e):
    btn2.configure(bg="green")          #syntax for hover effect

def on_leave2(e):
    btn2.configure(bg="burlywood")

def on_enter3(e):
    btn3.configure(bg="green")          #syntax for hover effect

def on_leave3(e):
    btn3.configure(bg="burlywood")

def on_entermul(e):
    btnmul.configure(bg="green")          #syntax for hover effect

def on_leavemul(e):
    btnmul.configure(bg="burlywood")

def on_enter0(e):
    btn0.configure(bg="green")          #syntax for hover effect

def on_leave0(e):
    btn0.configure(bg="burlywood")

def on_enterclr(e):
    btnclr.configure(bg="green")          #syntax for hover effect

def on_leaveclr(e):
    btnclr.configure(bg="burlywood")

def on_enterequal(e):
    btnequal.configure(bg="green")          #syntax for hover effect

def on_leaveequal(e):
    btnequal.configure(bg="burlywood")

def on_enterdiv(e):
    btndiv.configure(bg="green")          #syntax for hover effect

def on_leavediv(e):
    btndiv.configure(bg="burlywood")

def on_enterentry(e):
    entry1.configure(bg="gold")          #syntax for hover effect

def on_leaveentry(e):
    entry1.configure(bg="orange")

def on_entersin(e):
    btnsin.configure(bg="green")

def on_leavesin(e):
    btnsin.configure(bg="burlywood")


def on_entercos(e):
    btncos.configure(bg="green")


def on_leavecos(e):
    btncos.configure(bg="burlywood")


def on_entertan(e):
    btntan.configure(bg="green")


def on_leavetan(e):
    btntan.configure(bg="burlywood")


def on_entersqrt(e):
    btnsqrt.configure(bg="green")


def on_leavesqrt(e):
    btnsqrt.configure(bg="burlywood")


def on_enterlog(e):
    btnlog.configure(bg="green")


def on_leavelog(e):
    btnlog.configure(bg="burlywood")


###################################################################################

tex = StringVar()
operator =''  # operator is made if any thing is clicked the value will go to the operator variable

entry1 = Entry(screen, background="orange", font=('arial', 20), bd=40, justify='right',
               textvariable=tex)  # to enter the operations in the calculator
# textvariable is added to give the text
# and justify is used to start the txt from right
entry1.grid(row=0, columnspan=4)  # columnspan is used to add all the buttons below

# for row 1
btn7= Button(screen, text='7', font=('arial', 20), bd=10, padx=16, pady=13, command=lambda:click(7),activebackground='red',activeforeground='white',bg='burlywood')
# activebackground and activeforeground is used fo the buttons which are clicked or are active
# pad-x and pad-y is used to increase the height and width and command is used to perform the action when its clicked
btn7.grid(row=1, column=0)


btn8 = Button(screen, text='8', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(8),activebackground='red',activeforeground='white',bg='burlywood')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(9),activebackground='red',activeforeground='white',bg='burlywood')
btn9.grid(row=1, column=2)

btnplus = Button(screen, text='+', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click("+"),activebackground='red',activeforeground='white',bg='burlywood')
btnplus.grid(row=1, column=3)

# for row 2

btn4 = Button(screen, text='4', font=('arial', 20), bd=10, padx=16,pady=13,command=lambda:click(4),activebackground='red',activeforeground='white',bg='burlywood')  # padx and pady is used to increase the height and width
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(5),activebackground='red',activeforeground='white',bg='burlywood')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(6),activebackground='red',activeforeground='white',bg='burlywood')
btn6.grid(row=2, column=2)

btnsub = Button(screen, text='-', font=('arial', 20), bd=10, padx=19, pady=13,command=lambda:click("-"),activebackground='red',activeforeground='white',bg='burlywood')
btnsub.grid(row=2, column=3)

# for row 3

btn1 = Button(screen, text='1', font=('arial', 20), bd=10, padx=16,pady=13,command=lambda:click(1),activebackground='red',activeforeground='white',bg='burlywood')  # padx and pady is used to increase the height and width
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(2),activebackground='red',activeforeground='white',bg='burlywood')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('arial', 20), bd=10, padx=16, pady=13,command=lambda:click(3),activebackground='red',activeforeground='white',bg='burlywood')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text='*', font=('arial', 20), bd=10, padx=19, pady=13,command=lambda:click("*"),activebackground='red',activeforeground='white',bg='burlywood')
btnmul.grid(row=3, column=3)

# for row 4

btn0 = Button(screen, text='0', font=('arial', 20), bd=10, padx=16,pady=13,command=lambda:click(0),activebackground='red',activeforeground='white',bg='burlywood')  # padx and pady is used to increase the height and width
btn0.grid(row=4, column=0)

btnclr = Button(screen, text='C', font=('arial', 20), bd=10, padx=16, pady=13,command=clear,activebackground='red',activeforeground='white',bg='burlywood')
btnclr.grid(row=4, column=1)

btnequal = Button(screen, text='=', font=('arial', 20), bd=10, padx=16, pady=13,command=equal,activebackground='red',activeforeground='white',bg='burlywood')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text='/', font=('arial', 20), bd=10, padx=19, pady=13,command=lambda:click("-"),activebackground='red',activeforeground='white',bg='burlywood')
btndiv.grid(row=4, column=3)

#####################################################Advance calculation######################

btnsin = Button(screen, text='sin', font=('arial', 20), bd=10, padx=13, pady=18,command=cmsin,activebackground='red',activeforeground='white',bg='burlywood')
btnsin.grid(row=0, column=4)

btncos = Button(screen, text='cos', font=('arial', 20), bd=10, padx=12, pady=14,command=cmcos,activebackground='red',activeforeground='white',bg='burlywood')
btncos.grid(row=1, column=4)

btntan = Button(screen, text='tan', font=('arial', 20), bd=10, padx=13, pady=14,command=cmtan,activebackground='red',activeforeground='white',bg='burlywood')
btntan.grid(row=2, column=4)

btnsqrt = Button(screen, text='sqrt', font=('arial', 18), bd=10, padx=13, pady=15,command=cmsqrt,activebackground='red',activeforeground='white',bg='burlywood')
btnsqrt.grid(row=3, column=4)

btnlog = Button(screen, text='log', font=('arial', 20), bd=10, padx=12, pady=14,command=cmlog,activebackground='red',activeforeground='white',bg='burlywood')
btnlog.grid(row=4, column=4)

#########################################################################################

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)


entry1.bind('<Enter>',on_enterentry)               #for hover effect
entry1.bind('<Leave>',on_leaveentry)               #for hover effect

btn7.bind('<Enter>',on_enter7)               #for hover effect
btn7.bind('<Leave>',on_leave7)               #for hover effect

btn8.bind('<Enter>',on_enter8)               #for hover effect
btn8.bind('<Leave>',on_leave8)               #for hover effect

btn9.bind('<Enter>',on_enter9)               #for hover effect
btn9.bind('<Leave>',on_leave9)               #for hover effect

btnplus.bind('<Enter>',on_enterplus)               #for hover effect
btnplus.bind('<Leave>',on_leaveplus)               #for hover effect

btn4.bind('<Enter>',on_enter4)               #for hover effect
btn4.bind('<Leave>',on_leave4)               #for hover effect

btn5.bind('<Enter>',on_enter5)               #for hover effect
btn5.bind('<Leave>',on_leave5)               #for hover effect

btn6.bind('<Enter>',on_enter6)               #for hover effect
btn6.bind('<Leave>',on_leave6)               #for hover effect

btnsub.bind('<Enter>',on_entersub)               #for hover effect
btnsub.bind('<Leave>',on_leavesub)               #for hover effect

btn1.bind('<Enter>',on_enter1)               #for hover effect
btn1.bind('<Leave>',on_leave1)               #for hover effect

btn2.bind('<Enter>',on_enter2)               #for hover effect
btn2.bind('<Leave>',on_leave2)               #for hover effect

btn3.bind('<Enter>',on_enter3)               #for hover effect
btn3.bind('<Leave>',on_leave3)               #for hover effect

btnmul.bind('<Enter>',on_entermul)               #for hover effect
btnmul.bind('<Leave>',on_leavemul)               #for hover effect

btn0.bind('<Enter>',on_enter0)               #for hover effect
btn0.bind('<Leave>',on_leave0)               #for hover effect

btnclr.bind('<Enter>',on_enterclr)               #for hover effect
btnclr.bind('<Leave>',on_leaveclr)               #for hover effect

btnequal.bind('<Enter>',on_enterequal)               #for hover effect
btnequal.bind('<Leave>',on_leaveequal)               #for hover effect

btndiv.bind('<Enter>',on_enterdiv)               #for hover effect
btndiv.bind('<Leave>',on_leavediv)               #for hover effect

############################################################################################


screen.mainloop()  # to make the loop continous
