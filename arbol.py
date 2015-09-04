class Arbol:
  """Clase abstracta para Arboles generales"""
# ---------- metodos abstractos ----------
  def root(self):
    """Devuelve la raiz si no es vacio"""
    raise NotImplementedError('Debe ser implementado por una subclase')

  def parent(self, p):
    """Devuelve el padre de un nodo o None si es raiz"""
    raise NotImplementedError('Debe ser implementado por una subclase')

  def num_children(self, p):
    """Cantidad de hijos de p"""
    raise NotImplementedError('Debe ser implementado por una subclase')

  def children(self, p):
    """Hijos de p"""
    raise NotImplementedError('Debe ser implementado por una subclase')
  
  def __len__(self):
    """Cantidad de nodos en el Arbol"""
    raise NotImplementedError('Debe ser implementado por una subclase')

  # ---------- metodos concretos ----------
  def is_root(self, p):
    """True si es raiz"""
    return self.raiz() == p

  def is_leaf(self, p):
    """True si p es hoja"""
    return self.num_children(p) == 0

  def empty(self):
    """True si es vacio"""
    return len(self) == 0

