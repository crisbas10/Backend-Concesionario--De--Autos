class Vehiculo:
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

    def imprimir_data(self):
        print(
            f"el ID del vehiclo es {self.ID}, la marca del carro es un {self.Marca} , el modelo es {self.Modelo}, el año es {self.Año}, el precio de este vehiculo {self.Precio}, su kilometraje es {self.Kilometraje}, el estado de este vehiculo es {self.Estado}, y su disponibilidad es {self.Disponibilidad}  "
        )

    # creando los metodos faltantes de la clase
    def actualizar_precio(self, new_price):
        pass

    def cambiar_estado(self, state):
        pass


Carro1 = Vehiculo(
    "1001",
    "toyota",
    "montero",
    "2002",
    "27.000.000",
    "200.000",
    "usado",
    "True",
)
Carro1.imprimir_data()

Carro2 = Vehiculo(
    "1002",
    "ford",
    "fiesta",
    "2003",
    "10.000.000",
    "100.000",
    "usado",
    "True",
)
Carro2.imprimir_data()
