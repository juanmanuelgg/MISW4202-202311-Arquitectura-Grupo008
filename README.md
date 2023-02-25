# MISW4202-202311-Arquitectura-Grupo008-
Repositorio para el trabajo colaborativo del grupo 8 de curso ARQUITECTURAS ÁGILES DE SW.

## librerías
*pip install flask 
*pip install flask_sqlalchemy
*pip install flask_restful 
*pip install marshmallow_sqlalchemy


## Cola mensajeria - AZURE

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
