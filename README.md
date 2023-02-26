# MISW4202-202311-Arquitectura-Grupo008-
Repositorio para el trabajo colaborativo del grupo 8 de curso ARQUITECTURAS ÁGILES DE SW.

## librerías
```
pip install flask
pip install flask_sqlalchemy
pip install flask_restful
pip install marshmallow_sqlalchemy
pip install azure-storage-queue azure-identity
pip install celery
pip install redis
pip install requests
pip install psycop2
```


## Cola mensajeria - AZURE
orden de compra: https://portal.azure.com/#@uniandes.onmicrosoft.com/resource/subscriptions/5489bab2-15cb-4e9b-95e1-e04f88d2ca5a/resourceGroups/appsvc_linux_centralus_basic/providers/Microsoft.Storage/storageAccounts/proyectocpp001/overview

transporte: https://portal.azure.com/#@uniandes.onmicrosoft.com/resource/subscriptions/5489bab2-15cb-4e9b-95e1-e04f88d2ca5a/resourceGroups/appsvc_linux_centralus_basic/providers/Microsoft.Storage/storageAccounts/rutastransporteccp001/overview


```
az login
pip install azure-storage-queue azure-identity
```
 ## Leer la cola de mansajeria
```
  print("\nPeek at the messages in the queue...")

    # Peek at messages in the queue
    peeked_messages = queue_client.peek_messages(max_messages=5)

    for peeked_message in peeked_messages:
        # Display the message
        print("Message: " + peeked_message.content)
```

## App serive azure
### App service orden de compra : app-service-cpp-001.azurewebsites.net/ordencompra
### App service transporte : app-service-ccp-002.azurewebsites.net/transporte

![image](https://user-images.githubusercontent.com/60898371/221377028-e5304cad-1dcb-4ea8-a602-da14f8b3c131.png)

