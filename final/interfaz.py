from tkinter import *
from concurrent.futures import ThreadPoolExecutor
import threading
import random
import time
import sys
from  cliente import *
import numpy as np


raiz=Tk()
raiz.title("Cliente")
raiz.resizable(0,0)
raiz.geometry("200x200")
raiz.config(bg="black")

a_m=IntVar()
a_n=IntVar()

b_m=IntVar()
b_n=IntVar()


label3=Label(raiz, text="M")
label3.place(x=100,y=15)

label3=Label(raiz, text="N")
label3.place(x=130,y=15)

cuadro1=Entry(raiz,textvariable=a_m)
cuadro1.place(x=100,y=40,width=20,height=20)

cuadro2=Entry(raiz,textvariable=a_n)
cuadro2.place(x=130,y=40,width=20,height=20)

label1=Label(raiz, text="Matriz A: ")
label1.place(x=40,y=40)

cuadro3=Entry(raiz,textvariable=b_m)
cuadro3.place(x=100,y=70,width=20,height=20)

cuadro4=Entry(raiz,textvariable=b_n)
cuadro4.place(x=130,y=70,width=20,height=20)

label2=Label(raiz, text="Matriz B: ")
label2.place(x=40,y=70)

def dimension(a,b,c,d):
  global Matrix_A
  global Matrix_B
  global Matrix_C
  Matrix_A = np.random.random((a,b))
  Matrix_A = Matrix_A * 10 
  Matrix_A = Matrix_A.astype(int) 

  Matrix_B = np.random.random((c,d))
  Matrix_B = Matrix_B * 10
  Matrix_B = Matrix_B.astype(int) 

  Matrix_C = np.zeros((a,d))
  Matrix_C = Matrix_C.astype(int)

def codbot():
    fila_a=a_m.get()
    fila_a2=a_n.get()
    
    fila_b=b_m.get()
    fila_b2=b_n.get()

    if fila_a2!=fila_b or fila_a2==0 or fila_a==0 or fila_b2==0 or fila_b==0 :
        error=Tk()
        error.title("ERROR")
        error.resizable(0,0)
        error.geometry("300x100")
        finerror=Label(error, text="esta matriz no es valida \n ingrese una nueva",font=("Cambria",13))
        finerror.place(x=50,y=30)
        exit()
        error.mainloop()
    dimension(fila_a,fila_a2,fila_b,fila_b2)
    c = Cliente(Matrix_A,Matrix_B,Matrix_C)



def codbot2():
    a_m.set(0)
    a_n.set(0)
    b_m.set(0)
    b_n.set(0)
    
envio=Button(raiz,text="Enviar",command=codbot)
envio.place(x=40,y=100)

limpiar=Button(raiz,text="limpiar",command=codbot2)
limpiar.place(x=100,y=100)


raiz.mainloop()
