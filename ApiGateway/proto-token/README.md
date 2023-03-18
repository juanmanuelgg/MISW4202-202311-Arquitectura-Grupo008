# Instrucciones para el uso del server http proto-token.

## 1. Instalar dependencias.

```bash
npm ci
```

## 2. Ejecutar en desarrollo.

```bash
npm start
```

### Modo de uso.

> docs/proto-token.postman_collection.json

## 3. Crear ejecutable.

```bash
npm run build
```

### Ubicacion del ejecutable.

> dist/proto-token.cjs

### Variables de entorno usadas.

| Variable     | uso                                       | valor por defecto |
| ------------ | ----------------------------------------- | ----------------- |
| PROTO_PORT   | Puerto por el que se expone la aplicación | 3000              |
| PROTO_SECRET | Secreto con el que se encripta el JWT.    |                   |
