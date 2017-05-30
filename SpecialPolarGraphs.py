import tkinter
import random
import time
root = tkinter.Tk()
root.title('Polar Graph Game')
root.configure(background = 'black')
def ln():
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    eq.configure(text = 'rcosΘ =' + a)
def crc():
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    #eq.configure(text = u)
#a = [line, circle, cardioid, limacon, lemniscate, rose]
def lemniscate():
    x = randint
front = tkinter.Label(root, text = (u"W\u207hat type of polar graph does this equation make?"), font = ('Courier', 20, 'bold'), background = 'black', foreground = 'white')
front.grid(row = 1, column = 1, columnspan = 11)
eq = tkinter.Label(root, font = ('Courier', 30), background = 'black', foreground = 'white')
eq.grid(row = 2, column = 1, columnspan = 7)
lin = tkinter.Button(root, text = 'line', font = ('Courier', 13), width = 12)
lin.grid(row = 3, column = 1)
circl = tkinter.Button(root, text = 'circle', font = ('Courier', 13), width = 12)
circl.grid(row = 3, column = 3)
card = tkinter.Button(root, text = 'cardioid', font = ('Courier', 13), width = 12)
card.grid(row = 3, column = 5)
lima = tkinter.Button(root, text = 'limacon', font = ('Courier', 13), width = 12)
lima.grid(row = 3, column = 7)
lem = tkinter.Button(root, text = 'lemniscate', font = ('Courier', 13), width = 12)
lem.grid(row = 3, column = 9)
ros = tkinter.Button(root, text = 'rose', font = ('Courier', 13), width = 10)
ros.grid(row = 3, column = 11)
root.mainloop()
