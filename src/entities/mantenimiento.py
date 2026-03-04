class Mantenimiento:
    """
    Representa un mantenimiento agendado para un vehículo.
    """

    def __init__(self, vehiculo: str, motivo: str, fecha: str) -> None:
        self._vehiculo = vehiculo
        self._motivo = motivo
        self._fecha = fecha
        self._estado = "Pendiente"

    def confirmar_mantenimiento(self) -> None:
        self._estado = "Confirmado"

    def mostrar_info(self) -> None:
        print("==== MANTENIMIENTO AGENDADO ====")
        print(f"Vehículo: {self._vehiculo}")
        print(f"Motivo: {self._motivo}")
        print(f"Fecha: {self._fecha}")
        print(f"Estado: {self._estado}")
