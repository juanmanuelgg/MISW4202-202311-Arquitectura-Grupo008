# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# class OrdenDeCompra(db.Model):
#    # __tablename__ = 'orden_compra'
#    id= db.Column( db.Integer, primary_key = True) 
#    producto = db.Column( db.String)
#    cliente=db.Column( db.String)
#    evidencia_fotografica=db.Column( db.String)
#    rutaPedido=db.Column( db.String)
#    estadoPedido=db.Column( db.String)
#    puntoVenta=db.Column(db.Integer)
#    precio=db.Column( db.String)  

   
# class OrdenDeCompraSchema(SQLAlchemyAutoSchema): 
#     class Meta:
#         model = OrdenDeCompra
#         include_relationships = True
#         load_instance = True