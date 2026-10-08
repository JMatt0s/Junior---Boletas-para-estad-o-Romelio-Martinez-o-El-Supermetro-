from getpass import getpass
from datetime import datetime
import secrets
import string

precio = {
    "Occidental": 100000,
    "Oriental": 50000,
    "Sur": 30000,
    "Norte": 30000,
}

def generar_factura(localidad, cantidad, total):
    fecha = datetime.now()
    nombre_localidad = localidad.replace(" ", "_").lower()
    nombre_archivo = (
        f"factura_{nombre_localidad}_{fecha:%Y%m%d_%H%M%S}_"
        f"{secrets.token_hex(3)}.txt"
    )
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=== FACTURA DE BOLETERIA ===\n")
        archivo.write(f"Fecha: {fecha:%d/%m/%Y %H:%M:%S}\n")
        archivo.write(f"Localidad: {localidad}\n")
        archivo.write(f"Cantidad de boletas: {cantidad}\n")
        archivo.write(f"Precio por boleta: ${precio[localidad]:,}\n")
        archivo.write(f"Total: ${total:,}\n")
        archivo.write("Estado: compra simulada; no es comprobante de pago real.\n")
    print(f"Factura guardada en: {nombre_archivo}")


def simular_pago_pse(total):
    bancos = {
        "1": "Banco Río Verde (ficticio)",
        "2": "Banco Montaña Azul (ficticio)",
        "3": "Banco Horizonte (ficticio)",
    }

    print("\n=== Pago PSE (DEMO) ===")
    print("No ingreses credenciales reales. Estos bancos y este inicio de sesion son ficticios.")
    for opcion, banco in bancos.items():
        print(f"{opcion}. {banco}")

    banco_seleccionado = bancos.get(input("Selecciona un banco: "))
    if banco_seleccionado is None:
        print("Banco no valido.")
        return

    print(f"\n=== Inicio de sesion: {banco_seleccionado} ===")
    usuario = input("Usuario ficticio: ")
    contrasena = getpass("Contrasena ficticia: ")
    if not usuario.strip() or not contrasena:
        print("Ingresa un usuario y una contrasena ficticios para continuar.")
        return

    print(f"\nConfirma el pago simulado de ${total}.")
    print("1. Autorizar pago")
    print("2. Rechazar pago")
    autorizacion = input("Elige una opcion: ")
    if autorizacion == "1":
        print("Pago PSE autorizado (simulacion; no se realizo ningun cobro).")
    elif autorizacion == "2":
        print("Pago PSE rechazado.")
    else:
        print("Opcion no valida. No se autorizo el pago.")


while True:
    print("\n=== ¡Junior Manda! ===")
    print(f"\n1. Occidental $100,000")
    print(f"2. Oriental $50,000")
    print(f"3. Sur $30,000")
    print(f"4. Norte $30,000")
    print("5. Salir")
    op=input("\nOpción: ")
    match op:
        case "1":
            localidad = "Occidental"
        case "2":
            localidad = "Oriental"
        case "3":
            localidad = "Sur"
        case "4":
            localidad = "Norte"
        case "5":
            print("SALIR DEL PROGRAMA")
            break
        case _:
            print("Elige una opción, intente de nuevo.")
            continue

    print(f"{localidad} ${precio[localidad]}")
    cantidad = int(input("Cantidad de boletas: "))
    total = precio[localidad] * cantidad
    print(f"Total a pagar: ${total}")
    generar_factura(localidad, cantidad, total)

    print("\n=== Metodo de Pago ===")
    print("1. Tarjeta de credito o debito")
    print("2. Nequi")
    print("3. PSE")
    print("4. Efecty")

    metodo_pago = input("Elige un metodo de pago: ")
    match metodo_pago:
        case "1":
            print("1. Tarjeta de credito")
            print("2. Tarjeta de debito")
            tipo_tarjeta = input("Elige el tipo de tarjeta: ")
            match tipo_tarjeta:
                case "1":
                    nombre_tarjeta = "credito"
                case "2":
                    nombre_tarjeta = "debito"
                case _:
                    print("Tipo de tarjeta no valido.")
                    continue

            print(f"\n=== Datos de tarjeta de {nombre_tarjeta} ===")
            print("DEMO: no ingreses datos reales; este programa no procesa pagos.")
            numero_tarjeta = getpass("Numero de tarjeta: ")
            mes_vencimiento = input("Mes de vencimiento (MM): ")
            year_vencimiento = input("Año de vencimiento (AAAA): ")
            cvv = getpass("CVV (3 o 4 digitos): ")

            if (
                not numero_tarjeta.replace(" ", "").isdigit()
                or not 13 <= len(numero_tarjeta.replace(" ", "")) <= 19
                or not mes_vencimiento.isdigit()
                or not 1 <= int(mes_vencimiento) <= 12
                or not year_vencimiento.isdigit()
                or len(year_vencimiento) != 4
                or not cvv.isdigit()
                or len(cvv) not in (3, 4)
            ):
                print("Datos de tarjeta no validos.")
                continue

            print(f"Pago simulado con tarjeta de {nombre_tarjeta}.")
        case "2":
            print("\n=== Pago con Nequi ===")
            print("DEMO: no ingreses tu numero real; este programa no procesa pagos.")
            telefono_nequi = input("Numero de celular registrado en Nequi (+57): ")
            telefono_limpio = telefono_nequi.replace(" ", "").replace("-", "")
            if not telefono_limpio.isdigit() or len(telefono_limpio) != 10 or not telefono_limpio.startswith("3"):
                print("Ingresa un numero celular de 10 digitos.")
                continue
            print("Solicitud de pago Nequi.")
        case "3":
            simular_pago_pse(total)
        case "4":
            codigo_efecty = (
                "".join(secrets.choice(string.ascii_uppercase) for _ in range(3))
                + "".join(secrets.choice(string.digits) for _ in range(2))
            )
            print("\n=== Pago en Efecty (DEMO) ===")
            print("Codigo de pago:", codigo_efecty)
            print(f"Valor a pagar: ${total}")
            print("Este codigo es simulado; no es valido para realizar un pago real.")
        case _:
            print("Metodo de pago no valido.")
        
