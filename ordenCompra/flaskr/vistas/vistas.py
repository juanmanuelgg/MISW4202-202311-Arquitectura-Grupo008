
from flask import request
from ..modelos import db, OrdenDeCompra, OrdenDeCompraSchema
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url= "https://proyectocpp001.queue.core.windows.net/"
queue_name="proyectocpp001"
default_credential="VdNWf4pM9SlkaV5tJt7M9nGM+tjto1ufdFJQStr55s8lssTzhNzdN9SDw+9AZRFKyHAYD86KHvBe+AStT7gJkg=="

orden_compra_schema= OrdenDeCompraSchema()

class VistaOrdenDeCompra(Resource):
    def post(self):
        nueva_orden = OrdenDeCompra(
            producto=request.json["producto"],
                                    cliente=request.json["cliente"], 
                                    evidencia_fotografica=request.json["evidencia_fotografica"],
                                    rutaPedido=request.json["rutaPedido"],
                                    estadoPedido =request.json["estadoPedido"],
                                    puntoVenta=request.json["puntoVenta"],
                                    precio=request.json["precio"]
                                    )
        db.session.add(nueva_orden)        
        db.session.commit()
        print('nueva orden de compora----------ID',nueva_orden.id)
                
        if(nueva_orden):
            queue_client = QueueClient(account_url, queue_name=queue_name ,credential=default_credential)
            # res= queue_client.create_queue()            
            message = "fechaOrden:" + datetime.utcnow().strftime('%m/%d/%Y') + ";"  +"IdOrdenCompra:" +str(nueva_orden.id) +";"  + "estado:" + nueva_orden.estadoPedido +";"  + "idPuntoVenta:" + str(nueva_orden.puntoVenta)
            queue_client.send_message(message)  
            print("\nReceiving messages from the queue...")  

        return orden_compra_schema.dump(nueva_orden)
    
    
    def get(self):
        return [orden_compra_schema.dump(ca) for ca in OrdenDeCompra.query.all()]
        