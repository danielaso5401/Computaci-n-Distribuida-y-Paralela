from tkinter import *
from concurrent.futures import ThreadPoolExecutor
import threading
import random
import time
import sys
from servidor import *
import numpy as np

def mult_par(start,end,mata,matb,matc):
    dimension_N=len(mata)
    dimension_M=len(mata[0])
    #dimension_R=dimension_M
    dimension_F=len(matb[0])
    for i in range(start,end):
        for j in range(dimension_N):
            for k in range(dimension_M):
                matc[i][j] += int(mata[i][k] * matb[k][j])
    return (matc)

raiz=Tk()
raiz.title("Servidor")
raiz.resizable(0,0)
raiz.geometry("500x300")
raiz.config(bg="black")

a=StringVar()
b=StringVar()

def recivir():
    global r
    s = Servidor()
    s.aceptarCon()
    r=s.procesarCon()
    a.set('('+str(len(r[0]))+","+ str(len(r[0][0]))+')')
    b.set('('+str(len(r[1]))+","+ str(len(r[1][0]))+')')
    
def most():
    print(r[0])
    e=r[0]
    root = Tk()
    root.title("matriz A")
    root.config(bg="black")
    for g in range(len(e)):
        for c in range(len(e[g])):
            cell = Entry(root, width=10)
            cell.grid(row=g, column=c)
            cell.insert(0, '{}'.format(e[g][c]))
    root.mainloop()
    
def most1():
    print(r[1])
    e=r[1]
    root = Tk()
    root.title("matriz B")
    root.config(bg="black")
    for g in range(len(e)):
        for c in range(len(e[g])):
            cell = Entry(root, width=10)
            cell.grid(row=g, column=c)
            cell.insert(0, '{}'.format(e[g][c]))
    root.mainloop()
def most2():
    mata=r[0]
    matb=r[1]
    matc=r[2]
    dimension_N=len(mata)
    dimension_M=len(mata[0])
    executor = ThreadPoolExecutor(max_workers=3)
    for j in range(3):
      task1 = executor.submit(mult_par, int((dimension_N/3) * j), int((dimension_M/3) * (j+1)),mata,matb,matc)
    matc=task1.result()
    print(matc)
    e=matc
    root = Tk()
    root.title("matriz C")
    root.config(bg="black")
    for g in range(len(e)):
        for c in range(len(e[g])):
            cell = Entry(root, width=10)
            cell.grid(row=g, column=c)
            cell.insert(0, '{}'.format(e[g][c]))
    root.mainloop()
    
    
label=Label(raiz, text="dimension de A ")
label.place(x=100,y=30)
cuadro1=Entry(raiz,textvariable=a)
cuadro1.place(x=200,y=30,width=30,height=20)


label=Label(raiz, text="dimension de B ")
label.place(x=300,y=30)
cuadro2=Entry(raiz,textvariable=b)
cuadro2.place(x=400,y=30,width=30,height=20)

ingresar=Button(raiz,text="ingresar matrices",command=recivir)
ingresar.place(x=200,y=60)
 
label1=Label(raiz, text="Matriz A")
label1.place(x=100,y=100)

label2=Label(raiz, text="Matriz B")
label2.place(x=300,y=100)

mostrar1=Button(raiz,text="mostrar matriz A",command=most)
mostrar1.place(x=100,y=140)

mostrar2=Button(raiz,text="mostrar matriz B",command=most1)
mostrar2.place(x=300,y=140)

multiplicar=Button(raiz,text="multiplicar",command=most2)
multiplicar.place(x=215,y=180)


raiz.mainloop()
