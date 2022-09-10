from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo

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
    data = {
        "id": id
        }
    return render_template("show.html", dojo = Dojo.dojos_with_ninjas(data))


##  guardar info del form para el dojo
@app.route('/dojos/new', methods = ['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect('/dojos')


if __name__ == "__main__":
    app.run(debug=True)

