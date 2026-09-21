from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/incidencia", methods=["POST"])
def crear_incidencia():

    Aula = request.form["aula"]
    Usuario = request.form["usuario"]
    Descripcion = request.form["descripcion"]

    print("Aula:" + Aula)
    print("Usuario:" + Usuario)
    print("Descripcion:" + Descripcion)

    return "Incidencia recibida"

if __name__ == "__main__":
    app.run(debug=True)