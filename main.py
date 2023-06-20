from modulo_1.daouser import Usuarios
from modulo_2.daoprod import Productos, Carrito
import getpass
import os

while True:
    print('¿Que deseas hacer?')
    print('1 Registar usuario')
    print('2 Ingresar')
    print('3 Salir\n')
    
    op = input("Ingrese numero de la opcion: ")

    if op == "1":
        os.system("cls")
        print('Registro de usuarios\n')
        username = input("Ingresa nombre usuario: ")
        password = getpass.getpass("Ingrese password: ")
        nombre = input("Ingrese nombre: ")
        lastname = input("ingrese apellido: ")
        usuario = Usuarios(username, password, nombre, lastname)
        usuario.registrar()
        False
    elif op == "2":
        False
        try:
            os.system("cls")
            print('Iniciar Sesion\n')
            username = input("Ingresa nombre usuario: ")
            password = getpass.getpass("Ingrese password: ")
            usuario = Usuarios(username, password)
            usuario.login()
        except Exception as e:
            print(type(e).__name__)
    
        while usuario.bool_user==True:
                try:
                    print('¿Que deseas hacer?\n ')
                    print('1 Registrar producto ')
                    print('2 Listar productos\n')
                    # print('3 Ver carrito \n')
                    op = input('Ingrese el numero de la opcion: ')

                    if op == "1":
                        print('Registrar producto\n')
                        idp = input("Ingrese ID: ")
                        name = input("Ingrese nombre: ")
                        precio = input("Ingrese precio: ")
                        stock = input("Ingrese stock: ")
                        producto = Productos(idp, name, precio, stock)
                        producto.registrar()

                    elif op == "2":
                        os.system('cls')
                        print('Listar productos\n')
                        productos = Productos()
                        productos.listar()
                        # print('')
                        # print('Elige un producto\n')
                        # op_prod = input("Ingrese id: ")
                        # carrito = Carrito()
                        # carrito.agregar_carrito(op_prod)

                    # elif op == "3":
                    #     print('Ver carrito\n')
                    #     carrito = Carrito()
                    #     carrito.listar_carrito()

                except Exception as e:
                    print(type(e).__name__)

        else:
            os.system("cls")
            print('Debes iniciar sesion')
            usuario.login()


    elif op == "3":
        False
        os.system("cls")
        print('Adios :3')
        exit()
        
    else:
        os.system("cls")
        print('Opcion no valida\n')