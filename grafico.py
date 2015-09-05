import pygame, os
from random import randint
import inputbox

#--------Arbol Binario de Busqueda--------
class NodoABB:
    def __init__(self,d, p=None):
        self.dato=d
        self.izq=None
        self.der=None
        self.padre=p
#----------------Arbol AVL----------------
class NodoAVL(NodoABB):
    def __init__(self,d, p=None):
        NodoABB.__init__(self,d,p)
        self.altura=-1
#--------Arbol rojo y negro--------
class NodoRN(NodoABB):
    def __init__(self,d):
        NodoABB.__init__(self, d)
        self.negro=False
Nulo=NodoRN(None)
Nulo.padre=Nulo
Nulo.izq=Nulo
Nulo.der=Nulo
Nulo.negro=True
def alt_negra(p):
    if p.izq!=Nulo or p.der!=Nulo: return 0
    alt=0
    while (p!=Nulo):
        alt+=p.negro
        p=p.padre
    return alt
            
  

def azar(arb, cant):
    for i in range(cant):
        arb.insertar(randint(1,200))
def borrazar(arb):
    for i in range(100):
        while a.raiz:
            n=a.buscar(randint(1,200))
            if n: #Cuando encuentra un numero que esta en el arbol
                break
        arb.borrar(n)


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (5,25)#Posicion inicial de la ventana

class Grafico:
    def __init__(self, W=800, H=600):
        self.screensize=[W,H]
        self.radio=13
        self.y_origen=100
        self.delta_y=100
        self.offset=[0,0]
        self.separacion=4 #numero mas alto es menos separacion
        self.screen = None
        self.ayuda=False
        self.textoAyuda="H: Mostrar/Ocultar ayuda\nA: Insertar nodo\nR:Insertar x nodos al azar\nD: Borrar nodo\nIzq./Der.: Juntar/esparcir nodos\nMouse (arrastrar): mover arbol\nEspacio: Recentrar arbol\nESC: Salir"
    def graficar(self, arb):
        assert hasattr(arb, 'raiz'), "El tipo arbol debe tener un atributo llamado \'raiz\'"
        pygame.init()
        scrolling=False
        self.screen= pygame.display.set_mode(self.screensize,pygame.RESIZABLE)
        pygame.display.set_caption("Grafico")
        self.dibujarArbol(arb)
        listo=False
        while not listo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    listo=True
                elif event.type==pygame.VIDEORESIZE:
                    self.screensize=event.dict['size']
                    screen=pygame.display.set_mode(self.screensize,pygame.RESIZABLE)
                    self.dibujarArbol(arb)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    scrolling=True
                elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                    scrolling=False
                    self.dibujarArbol(arb)
                elif event.type == pygame.MOUSEMOTION and scrolling:
                    self.offset[0]+=event.rel[0]
                    self.offset[1]+=event.rel[1]
                elif event.type == pygame.KEYDOWN:
                    
                        if event.key==pygame.K_ESCAPE:
                            listo=True
                            
                        elif event.key==pygame.K_h:
                            self.ayuda=not self.ayuda
                            
                        elif event.key==pygame.K_d:
                            n=inputbox.ask(self.screen, 'Eliminar numero')
                            if n:
                                n=int(n)
                                arb.borrar(n)
                            
                        elif event.key==pygame.K_LEFT:
                            if self.separacion<10:
                                self.separacion+=1
                            
                        elif event.key==pygame.K_RIGHT:
                            if self.separacion>1:
                                self.separacion-=1
                        elif event.key==pygame.K_SPACE:
                            self.offset=[0,0]
                        elif event.key==pygame.K_a:
                            n=inputbox.ask(self.screen, 'Insertar numero')
                            if n:
                                n=int(n)
                                arb.insertar(n)
                        elif event.key==pygame.K_r:
                            n=inputbox.ask(self.screen, 'Cant. de numeros a ingresar')
                            if n:
                                n=int(n)
                                azar(arb,n)
                        self.dibujarArbol(arb)                   
        pygame.display.quit()
        pygame.quit()

    def dibujarArbol(self, arb):
        self.screen.fill((125,125,125))
        if self.separacion==0: #Para evitar dividir por 0
            self.separacion=1
        self.dibujarNodo(arb.raiz, self.offset[0]+self.screensize[0]//2,self.offset[1]+self.y_origen,self.separacion)
        self.mostrarAyuda()
        pygame.display.flip()

    def dibujarNodo(self, nodo, x, y, depth, origen=None):
        if not nodo or nodo==Nulo or y>self.screensize[1]+self.radio:
            return #Si no existe o esta debajo de la pantalla, dejar de dibujar
        if origen: #Si existe el parametro origen, dibujar la linea que lleva hasta el mismo
            pygame.draw.line(self.screen,(255,255,255), (x,y-self.radio), origen)
        if isinstance(nodo, NodoRN):
            color=(25,25,25) if nodo.negro else(250,25,25)
        else:
            color=(100,100,100)
        if x<self.screensize[0]+self.radio and x>-self.radio and y>-self.radio:
            pygame.draw.circle(self.screen, (200,200,200), (x,y), self.radio)
            pygame.draw.circle(self.screen, color, (x,y), self.radio-1)
            font = pygame.font.SysFont("Arial", 12)
            dato = font.render(str(nodo.dato),True, (255,255,255))
            self.screen.blit(dato, (x-dato.get_width()//2,y-dato.get_height()//2))
            if isinstance(nodo, NodoRN):
                alt_n=alt_negra(nodo)
                if alt_n:
                    alt_n=font.render(str(alt_n),True, (255,255,255))
                    self.screen.blit(alt_n, (x+self.radio+alt_n.get_width()//2,y-dato.get_height()//2))
            elif isinstance(nodo, NodoAVL):
                alt=font.render(str(nodo.altura),True, (255,255,255))
                self.screen.blit(alt, (x+self.radio+alt.get_width()//2,y-dato.get_height()//2))
        self.dibujarNodo(nodo.izq, x-(self.screensize[0]/depth), y+self.delta_y,depth*2, (x,y+self.radio))
        self.dibujarNodo(nodo.der, x+(self.screensize[0]/depth), y+self.delta_y,depth*2, (x,y+self.radio))
    def mostrarAyuda(self):
        if(not self.ayuda):
            ayuda=self.textoAyuda.split('\n')[0]
        else:
            ayuda=self.textoAyuda
        font = pygame.font.SysFont("Arial", 12)
        y=5
        for linea in ayuda.split('\n'):
            linea=font.render(str(linea),True, (255,255,255))
            self.screen.blit(linea, (10,y+linea.get_height()//2))
            y+=15
            
