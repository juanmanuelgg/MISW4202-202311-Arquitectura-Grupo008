
from flask import request
from ..modelos import db, OrdenDeCompra, OrdenDeCompraSchema
from flask_restful import Resource
from datetime import datetime
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, JWTManager
from flask_restful import Resource

orden_compra_schema= OrdenDeCompraSchema()
class VistaOrdenDeCompra(Resource):
    
    def post(self):
        nueva_orden = OrdenDeCompra(
        vendedor_id_get = get_jwt_identity()

            producto=request.json["producto"],
                                    cliente=request.json["cliente"], 
                                    evidencia_fotografica=request.json["evidencia_fotografica"],
                                    rutaPedido=request.json["rutaPedido"],
                                    estadoPedido =request.json["estadoPedido"],
                                    puntoVenta=request.json["puntoVenta"],
                                    precio=request.json["precio"],
                                    vendedor_id = vendedor_id_get
                                    )
        db.session.add(nueva_orden)        
        db.session.commit()
        print('nueva orden de compora----------ID',nueva_orden.id)
                
        return orden_compra_schema.dump(nueva_orden)
    
    def get(self, id_vendedor_get):
        vendedor_id = get_jwt_identity()
        if id_vendedor_get == vendedor_id:
            return [orden_compra_schema.dump(ca) for ca in OrdenDeCompra.query.all.filter_by(vendedor_id = vendedor_id)]
        