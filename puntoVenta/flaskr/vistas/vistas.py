import uuid
from flask import request

from ..modelos import OrdenCompraShema, PuntoVentaShema, TransporteShema
from ..modelos import db, PuntoVenta,OrdenCompra,Transporte
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url_transporte= "https://proyectocpp001.queue.core.windows.net/"
queue_name_transporte="proyectocpp001"
default_credential_transporte="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

account_url_orden= "https://proyectocpp001.queue.core.windows.net/"
queue_name_orden="proyectocpp001"
default_credential_orden="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

punto_venta_schema = PuntoVentaShema()
orden_de_compra_schema = OrdenCompraShema()
transporte_schema = TransporteShema()

class VistaEstadoOrdenCompra(Resource):
    def get(self):
        queue_client_read = QueueClient(account_url_orden, queue_name=queue_name_orden ,credential=default_credential_orden)
        return [orden_de_compra_schema.dump(eo) for eo in OrdenCompra.query.all()]

class VistaConsultaRutas(Resource):
    def get(self):
        return [transporte_schema.dump(tr) for tr in Transporte.query.all()]


        