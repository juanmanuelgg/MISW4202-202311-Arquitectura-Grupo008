import uuid
from flask import request

from ..modelos import OrdenCompraShema, PuntoVentaShema, TransporteShema
from ..modelos import db, PuntoVenta,OrdenCompra,Transporte
from flask_restful import Resource
from datetime import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

account_url_transporte = "https://rutastransporteccp001.queue.core.windows.net/"
queue_name_transporte ="rutastransporteccp001"
default_credential_transporte ="DUCSgELLrsxSs9BcclKN28ZxfgCEIDFugPDX57JzmuPNUdfz70tS4twlBtZ3F+mhuMreTgRSKgOT+AStyOSmRg=="

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
        separador1 = ';'
        separador2 = ':'

        queue_client_read = QueueClient(account_url_transporte, queue_name=queue_name_transporte ,credential=default_credential_transporte)
        peeked_messages = queue_client_read.peek_messages(max_messages=5)

        print('Ingresamos al servicio')
        for peeked_message in peeked_messages:
            print('peeked_message: ' + peeked_message.content)
            cadena = peeked_message.content
            print('cadena: ' + cadena)
            if(separador1 in cadena):
                array_cadena = cadena.split(separador1)

                fecha_ruta = array_cadena[0].split(separador2)[1]
                id_orden_compra_aux = array_cadena[1].split(separador2)[1]
                estado_pedido_aux = array_cadena[2].split(separador2)[1]
                id_punto_venta = array_cadena[3].split(separador2)[1]
                id_ruta = array_cadena[4].split(separador2)[1]

                print('fecha_ruta: ' + fecha_ruta)
                print('id_orden_compra_aux: ' + id_orden_compra_aux)
                print('estado_pedido_aux: ' + estado_pedido_aux)
                print('id_punto_venta: ' + id_punto_venta)
                print('id_ruta: ' + id_ruta)

            #     nueva_ruta = PuntoVenta(
            #         fecha_ruta = fecha_ruta, 
            #         estado_pedido = estado_pedido_aux,
            #         id_orden_compra = id_orden_compra_aux,
            #         id_punto_venta = id_punto_venta,
            #         id_ruta = id_ruta
            #     )                                
            #     db.session.add(nueva_ruta)        
            
            # db.session.commit()
        return {"id_ruta": id_ruta}


        