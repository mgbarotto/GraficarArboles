from grafico import NodoRN as GNodoRN, Nulo as GNulo, Grafico

class ARN:
    Nulo=GNulo
    NodoRN=GNodoRN
    def __str__(self):
        return "Dato:"+str(self.dato)+"\nPadre: "+str(self.padre.dato)+"\nIzq: "+str(self.izq.dato)+"\nDer: "+str(self.der.dato)+"\nColor: "+ ('Negro' if self.negro else 'Rojo')
#--------------Constructor--------------
    def __init__(self, r=None):
        self.claseNodo=ARN.NodoRN
        self.size=0
        self.raiz=ARN.Nulo
        if r: self.insertar(r)
        
#----------Operaciones Basicas----------
    def insertar(self, z):
        self.size+=1
        if not isinstance(z,self.claseNodo):
            z=self.claseNodo(z)
        y=ARN.Nulo
        x=self.raiz
        while(x!=ARN.Nulo):
            y=x
            if(z.dato<x.dato):
                x=x.izq
            else:
                x=x.der
        z.padre=y
        if(y==ARN.Nulo):
            self.raiz=z
        elif (z.dato<y.dato):
            y.izq=z
        else:
            y.der=z
        z.der=ARN.Nulo
        z.izq=ARN.Nulo
        z.negro=False
        self.corregirInsercion(z)
    def corregirInsercion(self, z):
        while (not z.padre.negro):
            if (z.padre==z.padre.padre.izq):
                y=z.padre.padre.der
                if (not y.negro):
                    z.padre.negro=True
                    y.negro=True
                    z.padre.padre.negro=False
                    z=z.padre.padre
                else:
                    if (z==z.padre.der):
                        z=z.padre
                        self.rot_izq(z)
                    z.padre.negro=True
                    z.padre.padre.negro=False
                    self.rot_der(z.padre.padre)
            else:
                y=z.padre.padre.izq
                if (not y.negro):
                    z.padre.negro=True
                    y.negro=True
                    z.padre.padre.negro=False
                    z=z.padre.padre
                else:
                    if (z==z.padre.izq):
                        z=z.padre
                        self.rot_der(z)
                    z.padre.negro=True
                    z.padre.padre.negro=False
                    self.rot_izq(z.padre.padre)
        self.raiz.negro=True

        
    def borrar(self, z):
        """
        Borra un nodo del arbol
        Acepta un parametro de tipo nodo o un valor, que se busca en el arbol.
        """
        if not isinstance(z, self.claseNodo):
            z=self.buscar(z)
        if not z: return
        self.size-=1
        if(z.izq!=ARN.Nulo and z.der!=ARN.Nulo):
            y=self.minimo(z.der)
        else:
            y=z
        if (y.izq!=ARN.Nulo):
            x=y.izq
        else:
            x=y.der
        x.padre=y.padre
        if(y.padre==ARN.Nulo):
            self.raiz=x
        elif(y==y.padre.izq):
            y.padre.izq=x
        else:
            y.padre.der=x
        if(y!=z):
            z.dato=y.dato
        if(y.negro):
            self.corregirEliminar(x)
    def corregirEliminar(self, x):
            w=None
            while(x!=self.raiz and x.negro):
                if(x==x.padre.izq):
                    w=x.padre.der
                    if(not w.negro):
                        w.negro=True
                        x.padre.negro=False
                        self.rot_izq(x.padre)
                        w=x.padre.der
                    if(w.izq.negro and w.der.negro):
                        w.negro=False
                        x=x.padre
                    else:
                        if (w.der.negro):
                            w.izq.negro=True
                            w.negro=False
                            self.rot_der(w)
                            w=x.padre.der
                        w.negro=x.padre.negro
                        x.padre.negro=True
                        w.der.negro=True
                        self.rot_izq(x.padre)
                        x=self.raiz
                else:
                    w=x.padre.izq
                    if(not w.negro):
                        w.negro=True
                        x.padre.negro=False
                        self.rot_der(x.padre)
                        w=x.padre.izq
                    if(w.der.negro and w.izq.negro):
                        w.negro=False
                        x=x.padre
                    else:
                        if (w.izq.negro):
                            w.der.negro=True
                            w.negro=False
                            self.rot_izq(w)
                            w=x.padre.izq
                        w.negro=x.padre.negro
                        x.padre.negro=True
                        w.izq.negro=True
                        self.rot_der(x.padre)
                        x=self.raiz
            x.negro=True
    def rot_izq(self, x):
        y=x.der
        x.der=y.izq
        y.izq.padre=x
        y.padre=x.padre
        if (x.padre==ARN.Nulo):
            self.raiz=y
        elif (x==x.padre.izq):
            x.padre.izq=y
        else:
            x.padre.der=y
        y.izq=x
        x.padre=y
        #self.reRooteo()
    def rot_der(self, y):
        x=y.izq
        y.izq=x.der
        x.der.padre=y
        x.padre=y.padre
        if (y.padre==ARN.Nulo):
            self.raiz=x
        elif (y==y.padre.izq):
            y.padre.izq=x
        else:
            y.padre.der=x
        x.der=y
        y.padre=x
        #self.reRooteo()
    def reRooteo(self):
        while self.raiz.padre!=ARN.Nulo: #Reacomodar raiz
            self.raiz=self.raiz.padre     
    def inorder(self, p='root'):
        if p=='root': p=self.raiz
        if p == ARN.Nulo or not p:
            return
        self.inorder(p.izq)
        print (p.dato, ('negro' if p.negro else 'rojo'))
        self.inorder(p.der)
    def list_inorder(self, l=[], p='root'):
        if p=='root': p=self.raiz
        if p==ARN.Nulo or not p:
            return
        self.list_inorder(l,p.izq)
        l.append([p.dato,p.altura])
        self.list_inorder(l,p.der)


    def buscar(self, k, p='root'):
        if p=='root': p=self.raiz
        if p==ARN.Nulo: p=None
        if not p or k is p.dato:
            return p
        if k<p.dato:
            return self.buscar(k, p.izq)
        else: return self.buscar(k, p.der)


        
    def minimo(self, p):
        while p.izq!=ARN.Nulo:
            p=p.izq
        return p
    def maximo(self, p):
        while p.der!=ARN.Nulo:
            p=p.der
        return p




    
