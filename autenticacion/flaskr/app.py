from . import create_app
from .modelos import db
from flaskr.vistas import VistaAutenticar, VistaIntentos, VistaLista
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()   
   
api = Api(app)
api.add_resource(VistaAutenticar , '/autenticar', methods=['POST','GET'])
api.add_resource(VistaIntentos , '/intentos_visitantes', methods=['GET'])
api.add_resource(VistaLista , '/blacklist', methods=['GET'])
jwt = JWTManager(app)