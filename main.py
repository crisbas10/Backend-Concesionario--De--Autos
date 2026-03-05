from src.entities import cliente
from src.entities  import vehiculo
#from src.entities  import concesionario
from src.entities  import mantenimiento


clientes: dict[str, Cliente] = {}


def mostrar_encabezado(titulo: str) -> None:
    print("=" * 40)
    print(titulo)
    print("=" * 40)


def crear_cuenta() -> None:
    nuevo_usuario = input("Nuevo usuario: ").strip()

    if nuevo_usuario in clientes:
        print("Ese usuario ya existe.")
        return

    nueva_password = input("Nueva contraseña: ").strip()
    clientes[nuevo_usuario] = Cliente(nuevo_usuario, nueva_password)

    print("Cuenta creada correctamente.")


def iniciar_sesion() -> None:
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    if usuario in clientes and clientes[usuario].validar_login(password):
        print(f"\nBienvenido señor {usuario}")
        menu_usuario()
    else:
        print("Usuario o contraseña incorrectos.")


def mostrar_vehiculos_disponibles() -> None:
    almacen = Concesionario()

    # Vehículos de prueba
    almacen.almacen.append(
        Vehiculo(1001, "Toyota", "Montero", 2000, 35000000, 150000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1002, "Chevrolet", "Onix RS", 2024, 60000000, 30000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1003, "Mazda", "CX-5", 2022, 98000000, 20000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1004, "Renault", "Duster", 2023, 85000000, 10000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1005, "Kia", "Sportage", 2021, 92000000, 45000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1006, "Hyundai", "Tucson", 2024, 115000000, 5000, "Nuevo", True)
    )
    almacen.almacen.append(
        Vehiculo(1007, "Nissan", "Frontier", 2020, 105000000, 60000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1008, "Ford", "Ranger", 2022, 130000000, 25000, "Usado", True)
    )
    almacen.almacen.append(
        Vehiculo(1009, "BYD", "Yuan Plus", 2024, 145000000, 0, "Nuevo", True)
    )
    almacen.almacen.append(
        Vehiculo(1010, "Volkswagen", "Jetta", 2019, 72000000, 80000, "Usado", True)
    )

    while True:
        print("\nVehículos disponibles:\n")

        disponibles = [v for v in almacen.almacen if v.disponible]

        if not disponibles:
            print("No hay vehículos disponibles.")
            return

        for vehiculo in disponibles:
            vehiculo.imprimir_data()
            print("-" * 50)

        try:
            id_compra = int(input("Ingrese el ID del vehículo que desea comprar: "))
        except ValueError:
            print("Ingrese un ID válido.")
            continue

        vehiculo_encontrado = None

        for vehiculo in disponibles:
            if vehiculo.ID == id_compra:
                vehiculo_encontrado = vehiculo
                break

        if vehiculo_encontrado:
            vehiculo_encontrado.disponible = False
            print("\n Compra realizada con éxito.")

            opcion = input(
                "\n1. Comprar otro vehículo\n2. Volver al menú principal\nSeleccione: "
            ).strip()

            if opcion == "1":
                continue
            else:
                break
        else:
            print("No existe un vehículo con ese ID.")


def menu_usuario() -> None:
    sesion_activa = True

    while sesion_activa:
        mostrar_encabezado("MENÚ")

        print("1. Realizar una compra")
        print("2. Agendar mantenimiento")
        print("3. Consultar estado")
        print("4. Stock de repuestos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_vehiculos_disponibles()

        if opcion == "2":
            print("==" * 20)
            print("   AGENDAR MANTENIMIENTO")
            print("==" * 20)

            vehiculo_mant = input("Ingrese su vehículo (marca/modelo): ").strip()
            motivo_mant = input("Ingrese el motivo del mantenimiento: ").strip()
            fecha_mant = input("Ingrese la fecha (DD/MM/AAAA): ").strip()

            # Crear y confirmar automáticamente
            nuevo_mantenimiento = Mantenimiento(vehiculo_mant, motivo_mant, fecha_mant)
            nuevo_mantenimiento.confirmar_mantenimiento()

            # Mostrar resumen
            print("\n Mantenimiento agendado con éxito.")
            nuevo_mantenimiento.mostrar_info()

        elif opcion == "5":
            print("Cerrando sesión...")
            sesion_activa = False

        else:
            print("Funcionalidad en desarrollo.")


def main() -> None:
    ejecutando = True

    while ejecutando:
        mostrar_encabezado("BYD MOTORS")

        print("1. Iniciar sesión")
        print("2. Crear cuenta")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            iniciar_sesion()

        elif opcion == "2":
            crear_cuenta()

        elif opcion == "3":
            print("Saliendo del sistema.")
            ejecutando = False

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()