
from flask import request
from ..modelos import db
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import create_access_token
from datetime import datetime


class VistaAutenticar(Resource):

    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        fecha_actual = datetime.now()     
        fecha_y_hora_en_texto = fecha_actual.strftime('%d/%m/%Y %H:%M')
        return {'mensaje': "login exitoso",
                'token_acceso': access_token,
                'fechaEmision': fecha_y_hora_en_texto,
                'fechaExpiracion': "",
                'rol': "Vendedor"
                }
