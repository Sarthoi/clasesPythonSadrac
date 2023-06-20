import json
import os

class Usuarios:
    
    def __init__(self,username,password,nombre=None,lastname=None) :
        self.username = username
        self.password = password
        self.nombre = nombre
        self.lastname = lastname
        
    def cargar_user(self):
        try:
            with open('./datos.json', 'r') as f:
                os.system('cls')
                data= json.load(f)
                f.close()
        except Exception as e:
            print(type(e).__name__)
        return data
    
    def guardar_user(self, data):
        try:
            with open('./datos.json', 'w') as f:
                json.dump(data,f)
                f.close()
                print('Registro exitoso\n')
        except Exception as e:
            print(type(e).__name__)
    
    def registrar(self):
        user_data={
            "username":self.username,
            "password":self.password,
            "nombre":self.nombre,
            "lastname":self.lastname
        }

        try:
            data=self.cargar_user()    
            data["usuarios"].append(user_data)
            self.guardar_user(data)
        except Exception as e:
            print(type(e).__name__)
        
    def login(self):
        data=self.cargar_user()
        self.bool_user=False
        for user in data['usuarios']:
            if user['username']== self.username and user['password']==self.password:
                print(f'Hola {self.username}')
                self.bool_user=True
                return 
        
        print('Usuario o contraseña incorrectos\n')

