from arbol import Arbol
from grafico import *
from grafico import NodoABB as Nodo
class ABB(Arbol):
    def __init__(self, r=None, claseNodo=None):
        if claseNodo: self.claseNodo=claseNodo
        else: self.claseNodo=Nodo
        if r:
            self.size=1
            if not isinstance(r,self.claseNodo):
                r=self.claseNodo(r)
        else:
            self.size=0
        self.raiz=r
        
    def root(self):
        """Devuelve la raiz si no es vacio"""
        return self.raiz

    def parent(self, p):
        """Devuelve el padre de un nodo o None si es raiz"""
        return p.padre
    def children(self,p):
        return (p.izq, p.der)
    def num_children(self, p):
        """Cantidad de hijos de p"""
        c=0
        for i in self.children:
            if i: c+=1
        return 0
    
    def __len__(self):
        """Cantidad de nodos en el Arbol"""
        return self.size


    def inorder(self, p='root'):
        if p=='root': p=self.raiz
        if not p:
            return
        self.inorder(p.izq)
        print(p.dato)
        self.inorder(p.der)
    def buscar(self, k, p='root'):
        if p=='root': p=self.raiz
        if not p or k is p.dato:
            return p
        if k<p.dato:
            return self.buscar(k, p.izq)
        else: return self.buscar(k, p.der)
    def minimo(self, p):
        while p.izq:
            p=p.izq
        return p
    def maximo(self, p):
        while p.der:
            p=p.der
        return p
    def sucesor(self, p):
        if p.der:
            return minimo(p.der)
        tmp=p.padre
        while tmp and p==tmp.der:
            p=tmp
            tmp=tmp.padre
        return tmp
    def predecesor(self, p):
        if p.izq:
            return maximo(p.izq)
        tmp=p.padre
        while tmp and p==tmp.izq:
            p=tmp
            tmp=tmp.padre
        return tmp
    def insertar(self, z):
        self.size+=1
        if not isinstance(z,self.claseNodo):
            z=self.claseNodo(z)
        y=None
        x=self.raiz
        while x:
            y=x
            if z.dato<x.dato: x=x.izq
            else: x=x.der
        z.padre=y
        if not y:
            self.raiz=z
        elif z.dato<y.dato:
            y.izq=z
        else:
            y.der=z
    def borrar(self, z):
        """Borra un nodo del arbol
            Se deberia usar como borrar(buscar(valor))
        """
        if not isinstance(z, self.claseNodo):
            z=self.buscar(z)
        if not z: return
        self.size-=1
        if not z.izq:
            self.transplantar(z,z.der)
        elif not z.der:
            self.transplantar(z,z.izq)
        else:
            y=self.minimo(z.der)
            if y.padre is not z:
                self.transplantar(y,y.der)
                y.der=z.der
                y.der.padre=y
            self.transplantar(z,y)
            y.izq=z.izq
            y.izq.padre=y
    def transplantar(self, u,v):
        if not u.padre: #Si u es raiz, v es la nueva raiz
            self.raiz=v
        elif u==u.padre.izq:
            u.padre.izq=v
        else:
            u.padre.der=v
        if v:
            v.padre=u.padre

