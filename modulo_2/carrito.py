from daoprod import Productos

class Carrito(Productos):


    def __init__(self):
        self.cart=[]

    def agregar_carrito(self, product):
        self.cart.append(product)
        print('Se agrego al carrito')


    def listar_carrito(self,idp):
        
            try:
                data:self.cargar()
                for prod in data['productos']:
                    if prod['id'] == idp:
                        self
            except Exception as e:
                print(type(e).__name__)