#!/bin/bash -x

npm run build

# Ejecutar desde la ruta del archivo deploy.sh
if [ ! -f webpack.config.cjs ]; then exit 1; fi

# USER_API_GATEWAY es secreto y el archivo .pem debe ir el el .gitignore
zip -r dist dist
scp -i ../API-Gateway_key.pem dist.zip ${USER_API_GATEWAY}@api.arquitecturaccp.com:~
rm dist.zip
ssh -i ../API-Gateway_key.pem ${USER_API_GATEWAY}@api.arquitecturaccp.com 'unzip dist.zip && rm dist.zip && chmod 744 dist/*.sh && cd dist && ./start.sh'

read -p "¿Quieres acceder a la máquina? (Yy/Nn)" -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd ..
    ./acceder-apigateway.sh
fi