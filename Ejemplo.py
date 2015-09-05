from ABB import *
from AVL import *
from ARN import *
if __name__=='__main__':
    print ("Que tipo de arbol?")
    print ("1-Binario de busqueda")
    print ("2-AVL")
    print ("3-Rojo y negro")
    while True:
        tipo=int(raw_input("Ingrese opcion: "))
        if 1<=tipo<=3:
            break
    a=None
    if tipo==1:
        a=ABB()
    elif tipo==2:
        a=AVL()
    else:
        a=ARN()
    g=Grafico()
    g.graficar(a)
    
