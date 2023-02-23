from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class OrdenDeCompra(db.Model):
   id= db.Column( db.Integer, primary_key = True) #10
   producto =db.Column( db.String)
   cliente=db.Column( db.String)
   evidencia_fotografica=db.Column( db.String)
   rutaPedido=db.Column( db.String)
   estadoPedido=db.Column( db.String)
   puntoVenta=db.Column(db.String) #relacionar con id del punto de venta
   precio=db.Column( db.String)
   
class Transporte(db.Model):
   id= db.Column( db.Integer, primary_key = True)
   rutaPedido =db.Column( db.String)
   
class PuntoDeVenta(db.Model):
   id=db.Column(db.Integer, primary_key = True) #
   ordenDeCompra=db.Column(db.Integer) # relacion con orden de compra con el id 10
   nombrePuntoVenta=db.Column(db.String)
#    estadoPedido=db.Column(db.String)
#    idPedido=(db.Integer)
#    ubicacionPuntoDeVenta=db.Column(db.String)
#    vendedor=db.Column( db.String)
#    rutaPedido=db.Column(db.String)
   

   
class OrdenDeCompraSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = OrdenDeCompra
        include_relationships = True
        load_instance = True
   
   