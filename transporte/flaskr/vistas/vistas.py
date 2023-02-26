
from flask import request
from ..modelos import db, Transporte, TransporteSchema
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url= "https://rutastransporteccp001.queue.core.windows.net/"
queue_name="rutastransporteccp001"
default_credential="DUCSgELLrsxSs9BcclKN28ZxfgCEIDFugPDX57JzmuPNUdfz70tS4twlBtZ3F+mhuMreTgRSKgOT+AStyOSmRg=="

account_url_read= "https://proyectocpp001.queue.core.windows.net/"
queue_name_read="proyectocpp001"
default_credential_read="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

transporte_schema= TransporteSchema()

class VistaTransporte(Resource):
    def get(self):
        return [transporte_schema.dump(ca) for ca in Transporte.query.all()]
    
    def post(self):    
        #Leer de la cola 
        queue_client_read = QueueClient(account_url_read, queue_name=queue_name_read ,credential=default_credential_read)
        print("\nPeek at the messages in the queue...")

        # Peek at messages in the queue
        peeked_messages = queue_client_read.peek_messages(max_messages=5)
        separador1 = ';';
        separador2 = ':';

        for peeked_message in peeked_messages:
            # Display the message
            print("Message: " + peeked_message.content)
            cadena = peeked_message.content
            if(separador1 in cadena):
                array_cadena = cadena.split(separador1)

                print(array_cadena)

                fecha = array_cadena[0]
                id_orden_compra_aux = array_cadena[1].split(separador2)[1]
                estado_pedido_aux = array_cadena[2].split(separador2)[1]

                nueva_ruta = Transporte(
                    fecha_orden = fecha,
                    fecha_ruta = request.json["fecha"], 
                    estado_pedido = estado_pedido_aux,
                    id_orden_compra = id_orden_compra_aux,
                    id_punto_venta = 1,
                    id_ruta = 1
                )                                
                db.session.add(nueva_ruta)        
            
            db.session.commit()
                
        if(nueva_ruta):
            queue_client = QueueClient(account_url, queue_name=queue_name ,credential=default_credential)
            message = str(datetime.utcnow()) + ";"  +"IdOrdenCompra:" +str(nueva_ruta.id_orden_compra) +";"  + "estadoPedido:" + nueva_ruta.estado_pedido  
            queue_client.send_message(message)  
            print("\nReceiving messages from the queue...")  

        return transporte_schema.dump(nueva_ruta)