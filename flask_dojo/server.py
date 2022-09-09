from flask import Flask, render_template, request, redirect

from ninja import Dojo

app = Flask(__name__)

##ruta home al iniciar server
@app.route('/')
def start_app():
    return redirect ('/dojos')

## ruta para traer pagina de dojo
@app.route('/dojos')
def dojo_page():
    return render_template ("dojo.html", dojos = Dojo.get_dojos())

##Mostrar info por Dojo
@app.route('/dojos/<int:id>')
def show_dojo(id):
    dojo = {
        "id": id
        }
    result = Dojo.show_info(dojo)
    return render_template("show.html", result = result)


##  guardar info del form para el dojo
@app.route('/dojos/new', methods = ['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect('/dojos')


if __name__ == "__main__":
    app.run(debug=True)
