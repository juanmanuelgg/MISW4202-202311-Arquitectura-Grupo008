import uuid
from flask import request

from ..modelos import OrdenCompraShema, PuntoVentaShema, TransporteShema
from ..modelos import db, PuntoVenta,OrdenCompra,Transporte
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage
import json

account_url_transporte= "https://proyectocpp001.queue.core.windows.net/"
queue_name_transporte="proyectocpp001"
default_credential_transporte="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

account_url_orden= "https://proyectocpp001.queue.core.windows.net/"
queue_name_orden="proyectocpp001"
default_credential_orden="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

punto_venta_schema = PuntoVentaShema()
orden_de_compra_schema = OrdenCompraShema()
transporte_schema = TransporteShema()


## cola orden de compra
account_url_read= "https://proyectocpp001.queue.core.windows.net/"
queue_name_read="proyectocpp001"
default_credential_read="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="


class VistaEstadoOrdenCompra(Resource):
    
    
    def get(self,id_orden_compra):
    
        queue_client_read = QueueClient(account_url_read, queue_name=queue_name_read ,credential=default_credential_read)
        peeked_messages = queue_client_read.peek_messages(max_messages=5)
        
     
        encontrado ={}
        for peeked_message in peeked_messages:   
            print('peeked_message',peeked_message.content)
            esta= "IdOrdenCompra:"+str(id_orden_compra)  in peeked_message.content         
            if(esta): 
                string="{"+ str(peeked_message.content).replace(";",",")+"}"
                print(string)
                return peeked_message.content

class VistaConsultaRutas(Resource):
    def get(self):
        queue_client_read = QueueClient(account_url_orden, queue_name=queue_name_orden ,credential=default_credential_orden)
        return [transporte_schema.dump(tr) for tr in Transporte.query.all()]


        