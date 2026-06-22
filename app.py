from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def responder(mensaje):
    mensaje = mensaje.lower()

    if "horario" in mensaje:
        return "Abrimos de martes a domingo de 9:00 a 00:00"

    elif "carta" in mensaje:
        return "Tenemos hamburguesas, cachopos, tapas y menús del día"

    elif "gluten" in mensaje:
        return "Tenemos opciones sin gluten"

    elif "reserva" in mensaje:
        return "Dime día, hora y personas para la reserva"

    elif "hola" in mensaje:
        return "¡Hola! ¿En qué puedo ayudarte?"

    else:
        return "No lo he entendido. Pregunta por horario, carta o reservas."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mensaje = request.json["mensaje"]
    respuesta = responder(mensaje)
    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)