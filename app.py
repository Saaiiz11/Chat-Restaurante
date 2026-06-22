from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").lower()

    if "hola" in mensaje:
        return jsonify({"respuesta": "Hola 👋 soy el bot del restaurante"})

    if "horario" in mensaje:
        return jsonify({"respuesta": "Abrimos de 9:00 a 00:00"})

    if "carta" in mensaje:
        return jsonify({"respuesta": "Tenemos hamburguesas, tapas y menús"})

    if "reserva" in mensaje:
        return jsonify({"respuesta": "Dime día, hora y personas"})

    return jsonify({"respuesta": "No lo he entendido"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)