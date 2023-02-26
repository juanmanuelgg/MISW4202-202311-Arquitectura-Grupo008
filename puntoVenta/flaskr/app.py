from . import create_app
from .modelos import db, OrdenCompra,Transporte
from flaskr.vistas import VistaConsultaRutas,VistaEstadoOrdenCompra
from flask_restful import Api


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()   
   
api = Api(app)
api.add_resource(VistaConsultaRutas, '/consultaRuta')
api.add_resource(VistaEstadoOrdenCompra, '/EstadoOrdenCompra')