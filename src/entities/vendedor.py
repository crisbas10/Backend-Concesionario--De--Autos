from empleado import Empleado
from venta import Venta 

class Vendedor(Empleado):
    def__init__(self):
        super().__init__(nombre, telefono, correo, salario, cargo) #invoca al constructor de la clase padre (Empleado)
        self.ventas_realizadas = [] #lista para almacenar las ventas realizadas por el vendedor