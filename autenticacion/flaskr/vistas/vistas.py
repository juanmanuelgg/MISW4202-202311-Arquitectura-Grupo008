
from flask import request, jsonify
from ..modelos import db
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import datetime

secreto = 'frase-secreta'
limite_de_intentos = 10
lista_negra = dict()
intentos_visitantes = dict()


class VistaAutenticar(Resource):

    def post(self):
        # 1. Obtener información del visitante
        visitor_ip = ''
        taken_from = ''
        visitor_ip = request.environ['REMOTE_ADDR']
        taken_from = 'REMOTE_ADDR'
        # if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        #     visitor_ip = request.environ['REMOTE_ADDR']
        #     taken_from = 'REMOTE_ADDR'
        # else:
        #     # if behind a proxy
        #     visitor_ip = request.environ['HTTP_X_FORWARDED_FOR']
        #     taken_from = 'HTTP_X_FORWARDED_FOR'
        key_visitante = "{} {}".format(taken_from, visitor_ip)

        # 2. Verificar al visitante contra la lista negra.
        if key_visitante in lista_negra:
            return ({"message": "Blacklisted."}), 401

        # 3. Proceder con el intento de autenticación y aumentar el contador de intentos si falla o reset si es exitoso.
        # 3.1. Evaluar la cantidad de intentos fallidos y evaluar si entra a lista negra.
        username = request.json.get("username")
        password = request.json.get("password")
        if username != "test" or password != "test":
            if key_visitante in intentos_visitantes:
                intentos_visitantes[key_visitante] = intentos_visitantes[key_visitante] + 1
            else:
                intentos_visitantes[key_visitante] = 1

            if intentos_visitantes[key_visitante] >= limite_de_intentos:
                lista_negra[key_visitante]=''
            return ({"message": "Bad username or password"}), 401

        # 4. Reset intentos del visitante. Generar el token de autenticación.
        intentos_visitantes[key_visitante] = 0
        fecha_actual = datetime.now()
        fecha_y_hora_en_texto = fecha_actual.strftime('%d/%m/%Y %H:%M')

        payload = {'user_id': 1,
                   'fechaEmision': fecha_y_hora_en_texto,
                   'fechaExpiracion': '',
                   'rol': "vendedor"
                   }
        token = create_access_token(
            identity=1, additional_claims=payload)
        return jsonify(access_token=token)

    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        print('----token', current_user_id)
        return {'message': 'token valido', 'userid': current_user_id}, 200


class VistaIntentos(Resource):
    # @jwt_required()
    def get(self):
        return intentos_visitantes, 200


class VistaLista(Resource):
    # @jwt_required()
    def get(self):
        return lista_negra, 200
