import json
import os


class Productos:

    def __init__(self, idp=None, name=None, precio=None, stock=None):
        self.idp = idp
        self.name = name
        self.precio = precio
        self.stock = stock

    def cargar(self):
        try:
            with open('./prod.json', 'r') as f:
                data = json.load(f)
                f.close()
        except Exception as e:
            print(type(e).__name__)
        return data

    def guardar(self, data):
        try:
            with open('./prod.json', 'w') as f:
                json.dump(data, f)
                f.close()
                os.system('cls')
                print('Producto Registrado\n')
        except Exception as e:
            print(type(e).__name__)

    def registrar(self):
        producto = {
            'id': self.idp,
            'name': self.name,
            'precio': self.precio,
            'stock': self.stock
        }

        try:
            data = self.cargar()
            if 'productos' not in data:
                data['productos'] = []
            data['productos'].append(producto)
            self.guardar(data)
        except Exception as e:
            print(type(e).__name__)

    def listar(self):
        try:
            data = self.cargar()
            for prod in data['productos']:
                print('Codigo: ', prod['id'])
                print('Nombre: ', prod['name'])
                print('Precio: ', prod['precio'], 'USD' )
                print('Stock: ', prod['stock'])
                print()

        except Exception as e:
            print(type(e).__name__)


class Carrito:

    def __init__(self):
        self.cart = []

    def agregar_carrito(self, productoid):
        producto = Productos()
        data = producto.cargar()
        for prod in data['productos']:
            if prod['id'] == productoid:
                producto = Productos(
                    prod['id'], prod['name'], prod['precio'], prod['stock'])
                self.cart.append(producto)
                os.system("cls")
                print('Se agrego al carrito\n')
                return
        print('No se econtro el producto\n')

    def listar_carrito(self):
        try:
            if len(self.cart) == 0:
                # os.system('cls')
                print('El carrito esta vacio\n')
            else:
                os.system('cls')
                print('Carrito de productos\n')
                productos = Productos()
                data = productos.cargar()
                for productoid in self.cart:
                    for prod in data['productos']:
                        if prod['id'] == productoid:
                            print('ID:', prod['id'])
                            print('Nombre:', prod['name'])
                            print('Precio:', prod['precio'], 'USD')
                            print('Stock:', prod['stock'])
                            print('')
                            break

        except Exception as e:
            print(type(e).__name__)


