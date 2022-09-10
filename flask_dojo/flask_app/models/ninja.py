from flask_app.config.mysqlconnection import connectToMySQL

class Ninja: 
    def __init__(self, ninja):
        self.id = ninja['id']
        self.first_name = ninja['first_name']
        self.last_name = ninja['last_name']
        self.age = ninja['age']
        self.created_at = ninja['created_at']
        self.updated_at = ninja['updated_at']

##Crea instancia de Ninja
    @classmethod
    def save_ninja(cls, ninja):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_y_ninjas').query_db(query, ninja)