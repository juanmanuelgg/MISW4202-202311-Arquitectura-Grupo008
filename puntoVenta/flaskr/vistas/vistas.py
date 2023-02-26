
from flask import request

from puntoVenta.flaskr.modelos.modelos import OrdenCompraShema, PuntoVentaShema, TransporteShema
from ..modelos import db, PuntoVenta,OrdenCompra,Transporte
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url= "https://proyectocpp001.queue.core.windows.net/"
queue_name="proyectocpp001"
default_credential="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

punto_venta_schema = PuntoVentaShema()
orden_de_compra_schema = OrdenCompraShema()
transporte_schema = TransporteShema()

class VistaEstadoOrdenCompra(Resource):
    def get(self):
        return [orden_de_compra_schema.dump(eo) for eo in OrdenCompra.query.all()]

class VistaConsultaRutas(Resource):
    def get(self):
        return [transporte_schema.dump(tr) for tr in Transporte.query.all()]
        