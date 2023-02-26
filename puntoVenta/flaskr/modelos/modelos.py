from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class PuntoVenta(db.Model):
   # __tablename__ = 'PuntoVenta'
   idPuntoVenta= db.Column( db.Integer, primary_key = True) 
   nombrePuntoVenta = db.column(db.String)
   direccion = db.column(db.String)
   
class PuntoVentaShema(SQLAlchemy) :
    class Meta:
        model = PuntoVenta
        include_relationships = True
        load_instance = True
    
class OrdenCompra(db.Model):
   # __tablename__ = 'OrdenCompra'
   idOrdenCompra= db.Column( db.Integer, primary_key = True)
   idPuntoVenta = db.Column( db.Integer)
   EstadoPagado = db.Column( db.Boolean)
   FechaOrden =db.Column( db.DateTime)

class OrdenCompraShema(SQLAlchemy) :
    class Meta:
        model = OrdenCompra
        include_relationships = True
        load_instance = True

class Transporte(db.Model):
   # __tablename__ = 'Transporte'
   idTransporte= db.Column( db.Integer, primary_key = True) 
   idOrdenCompra = db.Column( db.Integer)
   idPuntoVenta=db.Column( db.Integer)
   estadoentregado=db.Column( db.Boolean)
   fechaEntrega=db.Column( db.DateTime)
   idRuta=db.Column( db.Integer)


class TransporteShema(SQLAlchemy) :
    class Meta:
        model = Transporte
        include_relationships = True
        load_instance = True



    

   

   
   