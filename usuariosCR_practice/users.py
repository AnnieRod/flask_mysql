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
        return connectToMySQL('users_schema').query_db(query, data)
