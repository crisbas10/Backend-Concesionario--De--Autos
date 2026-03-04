from persona import Persona

"""
Se puede crear para mas adelante un empleado mecanico y asigarle una clase transaccional

"""


class Empleado(Persona):
    def __init__(self, nombre, telefono, correo, salario, cargo):
        super().__init__(
            nombre, telefono, correo
        )  # invoca al constructor de la clase padre (Persona)
        self.salario = salario
        self.cargo = cargo
