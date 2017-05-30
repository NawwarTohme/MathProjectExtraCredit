import tkinter
import random
import time
root = tkinter.Tk()
root.title('Polar Graph Game')
root.configure(background = 'black')
b = [1, 2, 3]
c = ['+', '-']
d = [1, 2, 3, 4]
m = 0
def ln():
    x = random.randint(-20,20)
    y = random.randint(-20,20)
    h = random.randint(1, 3)
    if h == 1:
        eq.configure(text = ('rcosΘ = ' + str(x)))
    elif h == 2:
        eq.configure(text = ('rsinΘ = ' + str(x)))
    else:
        eq.configure(text = ('Θ = ' + str(x)))
def crc():
    x = random.randint(2, 20)
    y = random.randint(2, 20)
    q = random.randint(1, 3)
    if q == 1:
        eq.configure(text = ('r = ' + str(x)))
    elif q == 2:
        eq.configure(text = ('r = ' + random.choice(c) + '2' + str(x) + 'cosΘ'))
    else:
        eq.configure(text = ('r = ' + random.choice(c) + '2' + str(x) + 'sinΘ'))
def car():
    x = random.randint(2, 20)
    f = random.randint(1, 2)
    if f == 1:
        eq.configure(text = ('r = ' + str(x) + random.choice(c) + ' ' + str(x) + 'cosΘ'))
    else:
        eq.configure(text = ('r = ' + str(x) + random.choice(c) + ' ' + str(x) + 'sinΘ'))
def lime():
    x = random.randint(10, 20)
    y = random.randint(2, 9)
    l = random.randint(1, 4)
    if l == 1:
        eq.configure(text = (' r = ' + str(x) + ' ' + random.choice(c) + ' ' + str(y) + 'cosΘ'))
    elif l == 2:
        eq.configure(text = (' r = ' + str(x) + ' ' + random.choice(c) + ' ' + str(y) + 'sinΘ'))
    elif l == 3:
        eq.configure(text = (' r = ' + str(y) + ' ' + random.choice(c) + ' ' + str(x) + 'cosΘ'))
    else:
        eq.configure(text = (' r = ' + str(y) + ' ' + random.choice(c) + ' ' + str(x) + 'sinΘ'))
def lemn():
    x = random.randint(2,20)
    y = random.randint(2,20)
    u = random.randint(1, 2)
    if u == 1:
        eq.configure(text = ('r^2 = ' + str(x) + '^2sin2Θ'))
    else:
        eq.configure(text = ('r^2 = ' + str(x) + '^2cos2Θ'))
def rose():
    x = random.randint(2, 20)
    i = random.randint(1, 4)
    if i == 1:
        eq.configure(text = ('r = ' + str(x) + 'sin3Θ'))
    elif i == 2:
        eq.configure(text = ('r = ' + str(x) + 'cos3Θ'))
    elif i == 3:
        eq.configure(text = ('r = ' + str(x) + 'sin2Θ'))
    else:
        eq.configure(text = ('r = ' + str(x) + 'cos2Θ'))
def chooselin():
    global s
    global k
    global m
    if k == ln:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    rose()
def chooseros():
    global s
    global k
    global m
    if k == rose:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    crc()
def choosecirc():
    global s
    global k
    global m
    if k == crc:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    lime()
def chooselime():
    global s
    global k
    global m
    if k == lime:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    car()
def choosecar():
    global s
    global k
    global m
    if k == car:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    lemn()
def chooselemn():
    global s
    global k
    global m
    if k == lemn:
        m = m + 1
        won.config(text = 'wins = ' + str(m))
        root.update()
    else:
        w = 0
        won.config(text = 'wins = 0')
    random.choice(s)
    ln()
s = [ln, crc, car, lime, lemn, rose]
k = random.choice(s)
front = tkinter.Label(root, text = ("What type of polar graph does this equation make?"), font = ('Courier', 20, 'bold'), background = 'black', foreground = 'white')
front.grid(row = 1, column = 1, columnspan = 13)
eq = tkinter.Label(root, font = ('Courier', 30), background = 'black', foreground = 'white')
eq.grid(row = 2, column = 1, columnspan = 7)
lin = tkinter.Button(root, text = 'line', font = ('Courier', 13), width = 12, command = chooselin)
lin.grid(row = 3, column = 1)
circl = tkinter.Button(root, text = 'circle', font = ('Courier', 13), width = 12, command = choosecirc)
circl.grid(row = 3, column = 3)
card = tkinter.Button(root, text = 'cardioid', font = ('Courier', 13), width = 12, command = choosecar)
card.grid(row = 3, column = 5)
lima = tkinter.Button(root, text = 'limacon', font = ('Courier', 13), width = 12, command = chooselime)
lima.grid(row = 3, column = 9)
lem = tkinter.Button(root, text = 'lemniscate', font = ('Courier', 13), width = 12, command = chooselemn)
lem.grid(row = 3, column = 11)
ros = tkinter.Button(root, text = 'rose', font = ('Courier', 13), width = 10, command = chooseros)
ros.grid(row = 3, column = 13)
root.mainloop()
