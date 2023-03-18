from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

db = SQLAlchemy()

class Autenticar(db.Model):
   # __tablename__ = 'PuntoVenta'
   id= db.Column( db.Integer, primary_key = True) 
   username = db.column(db.String)
   password = db.column(db.String)
   
class AutenticarShema(SQLAlchemy) :
    class Meta:
        model = Autenticar
       # include_relationships = True
        load_instance = True
