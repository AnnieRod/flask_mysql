from mysqlconnection import connectToMySQL

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

    ##Mostrar info x cada dojo
    @classmethod
    def show_info(cls,dojo):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_y_ninjas').query_db(query, dojo)
        return cls(results[0])