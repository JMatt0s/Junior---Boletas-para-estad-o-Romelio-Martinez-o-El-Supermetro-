# 🎟️ Sistema de Boletería - Junior de Barranquilla

Sistema de boletería por consola desarrollado en **Python** para la venta de entradas a los partidos del Club Deportivo Popular Junior F.C. como proyecto universitario.

> 🦈 *¡Junior Manda!*

---

## 📋 Descripción

Este proyecto permite simular la gestión y venta de boletas para partidos de Junior en el Estadio Metropolitano Roberto Meléndez. Desde una interfaz de consola, el usuario puede consultar los partidos disponibles, elegir una localidad, comprar boletas y revisar o cancelar sus compras.

## ✨ Funcionalidades

- Ver la lista de partidos disponibles (rival, fecha y hora).
- Consultar localidades, precios y disponibilidad de cupos.
- Comprar boletas para un partido y una localidad.
- Calcular el valor total de la compra.
- Ver el historial de compras realizadas.
- Cancelar una compra (devuelve los cupos a la localidad).
- Menú interactivo por consola.

## 🏟️ Localidades de ejemplo

| Localidad  | Precio (COP) | Capacidad |
|------------|--------------|-----------|
| Norte      | $30.000      | 100       |
| Sur        | $30.000      | 100       |
| Oriental   | $50.000      | 80        |
| Occidental | $100.000     | 50        |

> Los valores son de ejemplo y se pueden modificar en el código.

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.10 o superior
- **Interfaz:** Consola (terminal)
- **Librerías:** solo la biblioteca estándar de Python (no requiere instalar nada extra)

## 📁 Estructura del proyecto

```
boleteria-junior/
│
├── main.py            # Punto de entrada y menú principal
├── partidos.py        # Gestión de partidos
├── boletas.py         # Lógica de compra y cancelación
├── datos/
│   └── datos.json     # Almacenamiento de partidos y compras (opcional)
└── README.md
```

> Ajusta esta estructura según los archivos reales de tu proyecto. Si todo está en un solo archivo, basta con `main.py`.

## 🚀 Instalación y ejecución

1. Verifica que tengas Python instalado:

   ```bash
   python --version
   ```

2. Clona el repositorio o descarga el proyecto:

   ```bash
   git clone https://github.com/tu-usuario/boleteria-junior.git
   cd boleteria-junior
   ```

3. Ejecuta el programa:

   ```bash
   python main.py
   ```

## 💻 Ejemplo de uso

```
===== BOLETERÍA JUNIOR DE BARRANQUILLA =====
1. Ver partidos disponibles
2. Comprar boletas
3. Ver mis compras
4. Cancelar compra
5. Salir

Seleccione una opción: 1

--- Partidos disponibles ---
1. Junior vs Millonarios  | 15/11/2026 | 8:00 PM
2. Junior vs Nacional     | 22/11/2026 | 6:00 PM
```

## 🧠 Conceptos aplicados

- Variables, listas y diccionarios
- Funciones y modularización
- Estructuras de control (`if`, `while`, `for`)
- Validación de entradas del usuario
- Manejo de errores con `try / except`
- (Opcional) Programación orientada a objetos y manejo de archivos JSON

## 🔮 Mejoras futuras

- Registro e inicio de sesión de usuarios.
- Generación de un comprobante de compra en archivo `.txt`.
- Descuentos para abonados.
- Interfaz gráfica o versión web.
- Conexión a una base de datos.

## 👥 Autores

- **Nombre Apellido** - [@usuario](https://github.com/usuario)
- **Nombre Apellido** - [@usuario](https://github.com/usuario)

**Universidad:** Nombre de la universidad
**Materia:** Programación - Laboratorio de Programacion
**Docente:** Ruiz Botero Wilmer Hernan
**Año:** 2026 - 2

## 📄 Licencia

Proyecto académico sin fines comerciales. Junior de Barranquilla es una marca de su respectivo propietario; este proyecto no tiene afiliación oficial con el club. (solo soy hicha del tiburon 🦈 ❤️)
