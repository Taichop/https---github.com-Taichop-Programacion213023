import tkinter as tk
#Clase usuario
class Usuario:
    def __init__(self):
        self.usuario = "programacion"
        self.password = "programacion"
#Metodo para validar el usuario y la contraseña
    def validar(self, usuario_ingresado, password_ingresado):
        if self.usuario == usuario_ingresado and self.password == password_ingresado:
            return True
        else:
            return False
#Clase ComputadorMantenimiento
class ComputadorMantenimiento:
    #variable de clase para asignar un consecutivo a cada computador como su codigo
    contador_computador = 0
    #variable de clase para almacenar los computadores en una lista
    matriz_computadores = []

    def __init__(self,_codigo, _hora_entrada, _valor_hora):
        self.codigo = _codigo
        self.hora_entrada = _hora_entrada
        self.valor_hora = _valor_hora
        self.hora_salida = 0

#Método registrar_entrada(hora)
        def registrar_entrada(self, hora):
            self.hora_entrada = hora

#Método registrar_salida(hora)
        def registrar_salida(self, hora):
            self.hora_salida = hora

#Método calcular_valor(hora_salida)
        def calcular_valor(self, hora_salida):
            self.hora_salida = hora_salida
            horas_totales=self.hora_salida - self.hora_entrada
            valor_final=horas_totales*self.valor_hora
            return valor_final

#Método obtener_codigo()
        def obtener_codigo(self):
            return self.codigo
