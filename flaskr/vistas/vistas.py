
# from flask import request
from ..modelos import db, OrdenDeCompra, OrdenDeCompraSchema
from flask_restful import Resource


orden_compra_schema= OrdenDeCompraSchema()

class VistaOrdenDeCompra(Resource):
    def get(self):
        return [orden_compra_schema.dump(ca) for ca in OrdenDeCompra.query.all()]
        