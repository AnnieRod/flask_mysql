from mysqlconnection import connectToMySQL

#Crea clase acorde a tabla de base de datos
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Método de clase para hacer consultas a la base y agregar instancias por usuario
    @classmethod
    def get_all(cls):
        query= "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

#Metodo de clase para INSERTAR un nuevo usuario a la base@classmethod
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        new_user = connectToMySQL('users_schema').query_db(query, data)
        return new_user

#Consulta y muestra datos de usuario acorde a ID
    @classmethod
    def show(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query, data)
        return cls(result[0])

#Actualiza/edita datos de un registro
    @classmethod
    def update_info(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

#elimina usuario
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query, data)
