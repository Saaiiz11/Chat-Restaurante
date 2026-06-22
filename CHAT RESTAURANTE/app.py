palabras_clave = {
    "horario": ["horario", "abrís", "abierto"],
    "carta": ["carta", "menu", "comida", "platos"],
    "gluten": ["gluten", "celiaco", "celíaco"],
    "reserva": ["reserva", "reservar", "mesa"]
}

info = {
    "horario": "Abrimos de martes a domingo de 9:00 a 00:00",
    "carta": "Tenemos hamburguesas, cachopos, tapas y menús del día",
    "gluten": "Tenemos opciones sin gluten",
    "reserva": "Dime día, hora y personas"
}

while True:
    mensaje = input("Cliente: ").lower()

    encontrado = False

    for categoria in palabras_clave:
        for palabra in palabras_clave[categoria]:
            if palabra in mensaje:
                print("Bot:", info[categoria])
                encontrado = True
                break

    if not encontrado:
        print("Bot: No lo he entendido.")
        print("Bot del restaurante activo")

reservas = []

while True:
    mensaje = input("Cliente: ").lower()

    if "reserva" in mensaje:
        print("Bot: Dime nombre, día, hora y personas separados por comas")
        datos = input("Datos: ")

        partes = datos.split(",")

        if len(partes) == 4:
            reserva = {
                "nombre": partes[0].strip(),
                "dia": partes[1].strip(),
                "hora": partes[2].strip(),
                "personas": partes[3].strip()
            }

            reservas.append(reserva)
            print("Bot: Reserva guardada ✔️")

        else:
            print("Bot: Formato incorrecto. Usa: nombre, día, hora, personas")

    elif "ver reservas" in mensaje:
        print("Bot: Estas son las reservas:")
        for r in reservas:
            print(r)

    else:
        print("Bot: Pregunta por reserva o escribe 'ver reservas'")