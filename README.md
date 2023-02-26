# MISW4202-202311-Arquitectura-Grupo008-
Repositorio para el trabajo colaborativo del grupo 8 de curso ARQUITECTURAS ÁGILES DE SW.

## librerías
```
pip install flask 
pip install flask_sqlalchemy
pip install flask_restful 
pip install marshmallow_sqlalchemy
```


## Cola mensajeria - AZURE

url :https://learn.microsoft.com/es-es/azure/storage/queues/storage-quickstart-queues-python?tabs=passwordless%2Croles-azure-portal%2Cenvironment-variable-windows%2Csign-in-visual-studio-code#create-a-queue

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

