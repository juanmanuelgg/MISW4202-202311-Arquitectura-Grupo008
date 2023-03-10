
import uuid
from flask import request
from ..modelos import db, Transporte, TransporteSchema
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url_transporte= "https://rutastransporteccp001.queue.core.windows.net/"
queue_name_transporte="rutastransporteccp001"
default_credential_transporte ="DUCSgELLrsxSs9BcclKN28ZxfgCEIDFugPDX57JzmuPNUdfz70tS4twlBtZ3F+mhuMreTgRSKgOT+AStyOSmRg=="

account_url_orden = "https://proyectocpp001.queue.core.windows.net/"
queue_name_orden ="proyectocpp001"
default_credential_orden ="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

transporte_schema= TransporteSchema()

class VistaTransporte(Resource):
    def get(self):
        return [transporte_schema.dump(ca) for ca in Transporte.query.all()]
    
    def post(self):    
        separador1 = ';'
        separador2 = ':'
        orden_ruta = 0
        id_ruta_uuid = str(uuid.uuid4())

        queue_client_read = QueueClient(account_url_orden, queue_name=queue_name_orden ,credential=default_credential_orden)
        peeked_messages = queue_client_read.peek_messages(max_messages=5)

        for peeked_message in peeked_messages:
            
            cadena = peeked_message.content
            if(separador1 in cadena):
                orden_ruta += 1 
                array_cadena = cadena.split(separador1)

                fecha_orden_aux = array_cadena[0].split(separador2)[1]
                id_orden_compra_aux = array_cadena[1].split(separador2)[1]
                estado_pedido_aux = "ENRUTADO";
                id_punto_venta_aux = array_cadena[3].split(separador2)[1]

                nueva_ruta = Transporte(
                    fecha_orden = fecha_orden_aux,
                    fecha_ruta = request.json["fecha"], 
                    estado_pedido = estado_pedido_aux,
                    id_orden_compra = id_orden_compra_aux,
                    id_punto_venta = id_punto_venta_aux,
                    orden = orden_ruta,
                    id_ruta = id_ruta_uuid
                )                                
                db.session.add(nueva_ruta)        
            
            db.session.commit()
                
        if(nueva_ruta):
            queue_client = QueueClient(account_url_transporte, queue_name=queue_name_transporte ,credential=default_credential_transporte)
            message = "fecha_ruta:" +str(datetime.utcnow().strftime('%m/%d/%Y')) + ";"  +"IdOrdenCompra:" +str(nueva_ruta.id_orden_compra) +";"  + "estado:" + str(nueva_ruta.estado_pedido) +";" + "IdPuntoVenta:" +  str(nueva_ruta.id_punto_venta) +";" + "IdRuta:" +  str(nueva_ruta.id_ruta)
            queue_client.send_message(message)  
            print("\nReceiving messages from the queue...")  

        return [transporte_schema.dump(ca) for ca in Transporte.query.filter_by(id_ruta=nueva_ruta.id_ruta)]