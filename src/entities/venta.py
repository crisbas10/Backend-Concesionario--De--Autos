from vendedor import Vendedor
from cliente import Cliente
from vehiculo import Vehiculo

"""
Esta es la clase venta, representa una tabla transaccional
en donde se registran las ventas realizadas por los vendedores a los clientes,
cada venta tiene un ID unico, el vendedor que realizo la venta, el cliente que compro el vehiculo, 
el vehiculo vendido, 
la fecha de la venta y el precio final de la venta.

"""


class Venta:
    def __init__(
        self,
        ID: int,
        Vendedor: Vendedor,
        Cliente: Cliente,
        Vehiculo: Vehiculo,
        Fecha: str,
        Precio_final: float,
        Metodo_pago: str,
    ):
        self.ID = ID
        self.Vendedor = Vendedor
        self.Cliente = Cliente
        self.Vehiculo = Vehiculo
        self.Fecha = Fecha
        self.Precio_final = Precio_final
        self.Metodo_pago = Metodo_pago

    # cual es la comision? se debatira mañana
    def calcular_comision(self):
        pass

    def generar_factura(self):
        # aqui se debe usar un json para generar la factura de venta con los datos del cliente, vendedor, vehiculo, fecha y precio final
        pass
