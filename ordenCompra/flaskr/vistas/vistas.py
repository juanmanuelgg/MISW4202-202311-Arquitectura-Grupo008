
from flask import request
from ..modelos import db, OrdenDeCompra, OrdenDeCompraSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager

orden_compra_schema= OrdenDeCompraSchema()

class VistaOrdenDeCompra(Resource):
    
    @jwt_required(optional=True)
    def post(self):
        vendedor_id_get = get_jwt_identity()
        print('----vendedor_id_get',vendedor_id_get)
        nueva_orden = OrdenDeCompra(
            producto=request.json["producto"],
            cliente=request.json["cliente"], 
            evidencia_fotografica=request.json["evidencia_fotografica"],
            rutaPedido=request.json["rutaPedido"],
            estadoPedido =request.json["estadoPedido"],
            puntoVenta=request.json["puntoVenta"],
            precio=request.json["precio"],
            vendedor_id = str(vendedor_id_get)
            )
        db.session.add(nueva_orden)        
        db.session.commit()
        print('nueva orden de compra----------ID',nueva_orden.id)
                
        return orden_compra_schema.dump(nueva_orden)
    
    @jwt_required(optional=True)
    def get(self):
        #id_vendedor_get = get_jwt_identity()
        return [orden_compra_schema.dump(ca) for ca in OrdenDeCompra.query.all()]
        