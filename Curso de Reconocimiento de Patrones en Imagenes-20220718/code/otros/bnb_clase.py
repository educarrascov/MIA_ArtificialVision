"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 TICS 585 - Reconocimiento de Patrones en imágenes

 Clase de ejemplo para insertar nodos en un árbol no balanceado
 Autor: Miguel Carrasco (05-08-2021)
 rev.1.0

"""

class new_node:
    def __init__(self, value, parent, level):
        self.value = value
        self.parent = parent
        self.level = level
        self.child = []
      
class tree:
    def __init__(self):
        self.head = None
        self.level = 0
        self.parent = None
        self.child = []
    
    def add_node(self, value, parent, level):

        if len(self.child) == 0:
            i_node = new_node(value, parent, level)
            self.child.append(i_node)
        else:
            for node in self.child:
                if node.parent == parent:
                    i_node = new_node(value, parent, level)
                    self.child.append(i_node)
                    return self
                else:
                    serch_node = tree.find_parent(self, parent)
                    tree.add_node(serch_node,value, parent, level)
                    return self
            
        return self
    

    def find_parent(self, parent):
        for node in self.child:
            if len(node.child)>0:
                if node.value == parent:
                    return node
                else:
                    tree.find_parent(node, parent)
                    return node
            else:
                if node.value == parent:
                    return node
                
    
    def print_tree(self):
        
        for element in self.child:
            if len(element.child)>0:
                tree.print_tree(element)
            print(f'parent: {element.parent} node:{element.value}')


arbol = tree() #creamos un nuevo arbol
arbol.add_node(2,1,2)
arbol.add_node(6,1,2)
arbol.add_node(7,1,2)
arbol.add_node(9,6,3)
arbol.add_node(19,6,3)
arbol.add_node(-2,19,3)
arbol.print_tree()



