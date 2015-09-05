from ABB import *
from grafico import *




class AVL(ABB):
#--------------Constructor--------------
    def __init__(self, r=None):
        """
        Inicializa a un arbol con raiz r (si r=None, arbol vacio)
        """
        self.claseNodo=NodoAVL
        ABB.__init__(self,r,self.claseNodo)
        self.act_altura(self.raiz)
        
#----------Operaciones Basicas----------
    def insertar(self, z):
        if not isinstance(z,self.claseNodo):
            z=self.claseNodo(z)
        ABB.insertar(self,z)
        self.act_altura(z)
        self.balancear(z.padre)
        
    def borrar(self, z):
        """
        Borra un nodo del arbol
        Acepta un parametro de tipo nodo o un valor, que se busca en el arbol.
        """
        if not isinstance(z, self.claseNodo):
            z=self.buscar(z)
        if not z: return
        self.size-=1
        if not z.izq:
            to_balance=z.padre
            self.transplantar(z,z.der)
            self.act_altura(to_balance)
            self.balancear(to_balance)    
        elif not z.der:
            to_balance=z.padre
            self.transplantar(z,z.izq)
            self.act_altura(to_balance)
            self.balancear(to_balance)
        else:
            y=self.minimo(z.der)
            to_balance=y
            if y.padre is not z:
                to_balance=y.padre
                self.transplantar(y,y.der)
                y.der=z.der
                y.der.padre=y
            self.transplantar(z,y)
            y.izq=z.izq
            y.izq.padre=y
            self.act_altura(to_balance)
            self.balancear(to_balance)
        
#------------Operaciones AVL------------
    def act_altura(self, p):        
        if p:
            p.altura= max(self.altura(p.izq), self.altura(p.der))+1
            self.act_altura(p.padre)
    def altura(self, p):
        if not p:
            return -1
        return p.altura
    def colg_izq(self, p, q=None):
        p.izq=q
        if not q: return
        q.padre=p
    def colg_der(self, p, q=None):
        p.der=q
        if not q: return
        q.padre=p

    def rot_izq(self, p):
        tmp=p.izq
        if p.padre:
            if p.padre.izq==p:
                self.colg_izq(p.padre,tmp)
            else:
                self.colg_der(p.padre,tmp)
        else:
            tmp.padre=None
        self.colg_izq(p,tmp.der)
    
        self.colg_der(tmp,p)
        self.act_altura(p)
        self.act_altura(tmp)
        

    def rot_der(self, p):
        tmp=p.der
        if p.padre:
            if p.padre.izq==p:
                self.colg_izq(p.padre,tmp)
            else:
                self.colg_der(p.padre,tmp)
        else:
            tmp.padre=None
        self.colg_der(p,tmp.izq)
        self.colg_izq(tmp,p)
        self.act_altura(p)
        self.act_altura(tmp)


    def d_rot_izq(self, p):
        self.rot_der(p.izq)
        self.rot_izq(p)
        
    def d_rot_der(self, p):
        self.rot_izq(p.der)
        self.rot_der(p)
    def reRooteo(self):
        while self.raiz.padre: #Reacomodar raiz
            self.raiz=self.raiz.padre     
    def inorder(self, p='root'):
        if p=='root': p=self.raiz
        if not p:
            return
        self.inorder(p.izq)
        print('(',p.dato,', ',p.altura,')')
        self.inorder(p.der)
    def list_inorder(self, l=[], p='root'):
        if p=='root': p=self.raiz
        if not p:
            return
        self.list_inorder(l,p.izq)
        l.append([p.dato,p.altura])
        self.list_inorder(l,p.der)
    def balanceado(self, r):
        if not r or not (r.izq and r.der): return True
        if r==self.raiz: self.act_altura(r)
        balance=r.izq.altura-r.der.altura
        return balance>-2 and balance<2 and self.balanceado(r.izq) and self.balanceado(r.der)
    def balancear(self, r):
        if not r: return
        if self.altura(r.izq)-self.altura(r.der)==2:
            if self.altura(r.izq.izq)>=self.altura(r.izq.der):
                #desequilibrio simple hacia izquierda
                self.rot_izq(r)                
            else:
                #desequilibrio doble hacia izquierda
                self.d_rot_izq(r)
        elif self.altura(r.der)-self.altura(r.izq)==2:
            if self.altura(r.der.der)>=self.altura(r.der.izq):
                #desequilibrio simple hacia derecha
                self.rot_der(r)
            else:
                #desequilibrio doble hacia derecha
                self.d_rot_der(r)
        self.reRooteo()
        self.balancear(r.padre)




   
