
from flask import request
from ..modelos import db
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import datetime

secreto = 'frase-secreta'
limite_de_intentos = 10


class VistaAutenticar(Resource):
    # TODO: Recuperar estas estructuras de un archivo o una tabla
    lista_negra = set()
    intentos_visitante = dict()

    def post(self):
        # 1. Obtener información del visitante
        visitor_ip = ''
        taken_from = ''
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            visitor_ip = request.environ['REMOTE_ADDR']
            taken_from = 'REMOTE_ADDR'
        else:
            # if behind a proxy
            visitor_ip = request.environ['HTTP_X_FORWARDED_FOR']
            taken_from = 'HTTP_X_FORWARDED_FOR'

        key_visitante = "{} {}".format(taken_from, visitor_ip)
        if key_visitante in self.lista_negra:
            return ({"message": "Blacklisted."}), 401

        # 2. Verificar al visitante contra la lista negra.

        # 3. Proceder con el intento de autenticación y aumentar el contador de intentos si falla o reset si es exitoso.
        # 3.1. Evaluar la cantidad de intentos fallidos y evaluar si entra a lista negra.
        username = request.json.get("username")
        password = request.json.get("password")
        if username != "test" or password != "test":
            if key_visitante in self.intentos_visitante:
                self.intentos_visitante[key_visitante] = self.intentos_visitante[key_visitante] + 1
            else:
                self.intentos_visitante[key_visitante] = 1

            if self.intentos_visitante[key_visitante] >= limite_de_intentos:
                self.lista_negra.add(key_visitante)
            return ({"message": "Bad username or password"}), 401
        else:
            self.intentos_visitante[key_visitante] = 0

        # 4. Generar el token de autenticación.
        fecha_actual = datetime.now()
        fecha_y_hora_en_texto = fecha_actual.strftime('%d/%m/%Y %H:%M')

        payload = {'user_id': 1,
                   'fechaEmision': fecha_y_hora_en_texto,
                   'fechaExpiracion': '',
                   'rol': "vendedor"
                   }
        token = create_access_token(
            identity=username, additional_claims=payload)
        return jsonify(access_token=token)

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print('----token', current_user)
        return {'message': 'token valido', 'userid': current_user}, 200
