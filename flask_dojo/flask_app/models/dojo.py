from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo: 
    def __init__(self, dojo):
        self.id = dojo['id']
        self.name = dojo['name']
        self.created_at = dojo['created_at']
        self.updated_at = dojo['updated_at']
        self.ninjas = []

    ##metodo para crear instancias de dojo con cada linea de info que llega
    @classmethod
    def get_dojos(cls):
        query= "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    ##Insertar y guardar valores para dojo
    @classmethod
    def save_dojo(cls,dojo):
        query = "INSERT INTO dojos(name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        new_dojo = connectToMySQL('dojos_y_ninjas').query_db(query, dojo)
        return new_dojo

    ##Unión de dojos y ninjas one-to-many para pasarlos por cada Dojo
    @classmethod
    def dojos_with_ninjas (cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo