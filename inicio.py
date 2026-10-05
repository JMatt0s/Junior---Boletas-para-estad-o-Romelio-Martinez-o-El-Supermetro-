
partidos_local_junior = [
    {"jornada": 4,  "rival": "Deportivo Pereira",   "dia_hora": "2026-10-14 16:30", "estadio": "Romelio Martínez"},
    {"jornada": 14, "rival": "Inter de Bogotá",     "dia_hora": "2026-10-10 18:10", "estadio": "Romelio Martínez"},
    {"jornada": 16, "rival": "Águilas Doradas",     "dia_hora": "2026-10-24 18:05", "estadio": "Romelio Martínez"},
    {"jornada": 18, "rival": "Cúcuta Deportivo",    "dia_hora": "2026-11-08 15:30", "estadio": "Romelio Martínez"},
]
def ver_titulos():
    print("\n=== TÍTULOS DE JUNIOR ===")
    print("\n=== Titulos de Junior de Barranquilla. ===")

def ver_partidos():
    matriz_partidos = [
        ["Jornada", "Visitante", "Fecha y hora", "Estadio"]
    ]

    for partido in partidos_local_junior:
        fila = [
            partido["jornada"],
            partido["rival"],
            partido["dia_hora"],
            partido["estadio"],
        ]
        matriz_partidos.append(fila)

    print("\n=== PARTIDOS DE JUNIOR COMO LOCAL ===")
    print("\n{:<10} | {:<22} | {:<16} | {}".format(*matriz_partidos[0]))
    print("-" * 85)

    for fila in matriz_partidos[1:]:
        print("{:<10} | {:<22} | {:<16} | {}".format(*fila))

while True:
    print("\n=== ¡Junior Manda! ===")
    print("\n1. Ver partidos")
    print("2. Ver títulos")
    print("3. Boleteria y Abonos")
    print("4. Productos sobre Junior")
    print("5. Ver Museo Robiblaco 'Micaela Lavalle de Mejía'")
    print("6. Salir")

    opcion = input("\nOpción: ")
    match opcion:
        case "1":
            ver_partidos()
        case "2":
            ver_titulos()
        case "3":
            print("Boletería y Abonos")
        case "4":
            print("Productos sobre Junior")
        case "5":
            print("Ver Museo Robiblaco 'Micaela Lavalle de Mejía'")
        case "6":
            print("SALIR DEL PROGRAMA")
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")
