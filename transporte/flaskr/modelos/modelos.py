from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Transporte(db.Model):
   #__tablename__ = 'transporte'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   fecha_orden = db.Column(db.String)
   fecha_ruta = db.Column(db.String)
   estado_pedido = db.Column(db.String)
   id_orden_compra = db.Column(db.Integer)  
   id_punto_venta = db.Column(db.Integer)  
   id_ruta = db.Column(db.Integer)

class TransporteSchema(SQLAlchemyAutoSchema): 
    class Meta:
        model = Transporte
        #include_relationships = True
        load_instance = True