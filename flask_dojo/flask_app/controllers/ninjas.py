from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja

## Ruta a pagina de NINJAS
@app.route('/ninjas')
def ninja_page():
    return render_template("index.html", dojos = Dojo.get_dojos())

##Ruta creación de ninjas
@app.route('/ninjas/new', methods = ['POST'])
def create_ninja():
    Ninja.save_ninja(request.form)
    return redirect ('/dojos')

if __name__ == "__main__":
    app.run(debug=True)
