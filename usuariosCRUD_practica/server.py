from flask import Flask, render_template, request, redirect, flash
from users import User
app = Flask(__name__)

# llamar al método de clase get all para obtener todos los users y mostrarlos en el template segun indicacion
@app.route('/users')
def users_table():
    users = User.get_all()
    return render_template("index.html", users = users)
            
#Una misma ruta permite renderizar el form de añadir usuarios y recibir la información del formulario segun tipo de solicitud
@app.route('/users/new', methods=["GET","POST"])
def create_user():
    if request.method == 'GET':
        return render_template ("add.html")
    
    elif request.method == 'POST':
        data = {
            "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]
    }
    result = User.save(data)
    #si no logra guardar datos en database muestra error ydeja en la misma pagina
    if result != False:
        return redirect('/users')

    else:
        flash('Error including a new user to database, try again','error')
        return redirect('/users/new')


##ruta para editar (actualizar) registro
@app.route('/users/<int:id>/edit')
def show_users(id):
    data = {
        "id": id
        }
    return render_template("edit.html", user = User.show(data))
    
@app.route('/users/edit_user', methods=['POST'])
def edit_info():
    User.update_info(request.form)
    return redirect('/users')

## ruta para mostrar informacion
@app.route('/users/<int:id>/show')
def show(id):
    data = {
        "id": id
        }
    return render_template("show.html", user = User.show(data))

## ruta para eliminar registro 
@app.route("/users/<int:id>/destroy")
def delete_user(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)