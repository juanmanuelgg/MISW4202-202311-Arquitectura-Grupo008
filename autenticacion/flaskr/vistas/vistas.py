
from flask import request
from ..modelos import db
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import datetime

secreto = 'frase-secreta'


class VistaAutenticar(Resource):

    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        if username != "test" or password != "test":
            return ({"message": "Bad username or password"}), 401

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
