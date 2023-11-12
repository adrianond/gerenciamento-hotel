from flask_restful import reqparse

class UsuarioRequest:
    
    
    @staticmethod
    def getArgumentsRequest():
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('login', type = str, required = True, help = "campo login é obrigatório")
        argumentos.add_argument('senha', type = str, required = True, help = 'Campo senha é obrigatório')
        return argumentos