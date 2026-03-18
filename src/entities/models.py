#aqui van las clases antiguas
# vehiculo, mantemiento, cliente, empleado, venta, etc.
# lo que importa es que vayan las clases del modelo de negocio y la clase Usuario junto con las que se menciono en el 
#mensaje de whatsapp y del documento del profesor

class Empleado():
    def __init__(self, nombre, telefono, correo, salario, cargo):
        super().__init__(
            nombre, telefono, correo
        )  # invoca al constructor de la clase padre (Persona)
        self.salario = salario
        self.cargo = cargo

class Empleado():
    def __init__(self, nombre, telefono, correo, salario, cargo):
        super().__init__(
            nombre, telefono, correo
        )  # invoca al constructor de la clase padre (Persona)
        self.salario = salario
        self.cargo = cargo

class Vehiculo():
    def __init__(
        self,
        ID: int,
        Marca: str,
        Modelo: str,
        Año: int,
        Precio: float,
        Kilometraje: int,
        Estado: str,
        Disponibilidad: bool,
    ):
        self.ID = ID
        self.Marca = Marca
        self.Modelo = Modelo
        self.Año = Año
        self.Precio = Precio
        self.Kilometraje = Kilometraje
        self.Estado = Estado
        self.Disponibilidad = Disponibilidad


