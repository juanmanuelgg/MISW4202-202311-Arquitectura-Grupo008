from . import create_app
from .modelos import db, OrdenDeCompra
from flaskr.vistas import VistaOrdenDeCompra
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()   
   
api = Api(app)
api.add_resource(VistaOrdenDeCompra, '/ordencompra')

jwt = JWTManager(app)
