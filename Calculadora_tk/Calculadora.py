from tkinter import *
import math

class Calculadora():
    def __init__(self):
        self.total = 0
        self.numActual = ""
        self.valor_ingresado = True
        self.chequeo = False
        self.op = ""
        self.resultado = False
        
           
    def numeroIngresado(self, num):
        self.resultado = False
        primerNum = visualNum.get()
        segundoNum = str(num)
        if self.valor_ingresado:
            self.numActual = segundoNum
            self.valor_ingresado = False
        else:
            if segundoNum == '.':
                if segundoNum in primerNum:
                    return 
            self.numActual = primerNum + segundoNum
        self.display(self.numActual)
        
    def resultadoTotal(self):
        self.resultado = True
        self.numActual = float(self.numActual)
        if self.chequeo == True:
            self.validaFuncion()
        else:
            self.total = float(visualNum.get())
         
    def validaFuncion(self):
        if self.op == "suma":
            self.total += self.numActual
        if self.op == "resta":
            self.total -= self.numActual
        if self.op == "multi":
            self.total *= self.numActual
        if self.op == "division":
            self.total /= self.numActual
        self.valor_ingresado = True
        self.chequeo = False
        self.display(self.total)
        
    def operacion(self, op):
        self.numActual = float(self.numActual)
        if self.chequeo:
            self.validaFuncion()
        elif not self.resultado:
            self.total = self.numActual
            self.valor_ingresado = True
        self.chequeo = True
        self.op = op
        self.resultado = False
    
           
    def clear(self):
        self.resultado = False
        self.numActual = "0"
        self.display(0)
        self.valor_ingresado = True
        
            
    def clearEntry(self):
        self.clear()
        self.total = 0
        
    
    def display(self, valor):
        visualNum.delete(0, END)
        visualNum.insert(0, valor)
        
    def negativoPositivo(self):
        self.resultado = False
        self.numActual = -(float(visualNum.get()))
        self.display(self.numActual)  
    
    def raizCuadrada(self):
        self.resultado = False
        self.numActual = math.sqrt(float(visualNum.get()))
        self.display(self.numActual) 

    def coma(self):
        self.resultado = False
        self.numActual = float(visualNum.get())
        self.display(self.numActual) 


funcion = Calculadora()
root = Tk()
root.title("Calculadora")
root.resizable(width = False, height = False)
calc = Frame(root)
calc.grid()


visualNum = Entry(calc, font=('arial', 20, 'bold'), bg ="powder blue", bd = 30, width = 22, justify = RIGHT)
visualNum.grid(row = 0, column = 0, columnspan = 4, pady = 1)
visualNum.insert(0, "0")


#=============================================Fila1============================================================

botonClearEntry = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="CE", command = funcion.clearEntry).grid(row = 1,column = 0)
              
botonClear = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="C", command = funcion.clear).grid(row = 1,column = 1)
              
botonRaiz = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="√", command = funcion.raizCuadrada).grid(row = 1,column = 2)
              
botonSuma = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="+", command = lambda: funcion.operacion("suma")).grid(row = 1,column = 3)
              
#=============================================Fila2============================================================

boton7 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="7", command = lambda: funcion.numeroIngresado(7)).grid(row = 2,column = 0)

boton8 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="8", command = lambda: funcion.numeroIngresado(8)).grid(row = 2,column = 1)

boton9 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="9", command = lambda: funcion.numeroIngresado(9)).grid(row = 2,column = 2)
              
botonResta = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="-", command = lambda: funcion.operacion("resta")).grid(row = 2,column = 3)
              
#=============================================Fila3============================================================

boton4 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="4", command = lambda: funcion.numeroIngresado(4)).grid(row = 3,column = 0)

boton5 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="5", command = lambda: funcion.numeroIngresado(5)).grid(row = 3,column = 1)

boton6 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="6", command = lambda: funcion.numeroIngresado(6)).grid(row = 3,column = 2)
              
botonMult = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="*", command = lambda: funcion.operacion("multi")).grid(row = 3,column = 3)
              
#=============================================Fila4============================================================

boton1 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="1", command = lambda: funcion.numeroIngresado(1)).grid(row = 4,column = 0)

boton2 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="2", command = lambda: funcion.numeroIngresado(2)).grid(row = 4,column = 1)

boton3 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="3", command = lambda: funcion.numeroIngresado(3)).grid(row = 4,column = 2)
              
botonDiv = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="/", command = lambda: funcion.operacion("division")).grid(row = 4,column = 3)

#=============================================Fila5============================================================

boton0 = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="0", command = lambda: funcion.numeroIngresado(0)).grid(row = 5,column = 0)

botonComa = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text=",", command = funcion.coma).grid(row = 5,column = 1)

botonMasMenos = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text=chr(177), command = funcion.negativoPositivo).grid(row = 5,column = 2)
              
botonIgual = Button(calc, pady=1, bd=4, fg="black", font=('arial', 18, 'bold'), width = 6, height =2, 
              text="=", command = funcion.resultadoTotal).grid(row = 5,column = 3)




root.mainloop()