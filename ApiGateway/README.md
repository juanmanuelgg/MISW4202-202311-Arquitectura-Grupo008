# Configuración de nginx como API-Gateway

## Máquina virtual utilizada

![VM-API-Gateway](./VM-API-Gateway.png)

## Configuracion de los DNS Records del dominio del experimento

![DNS-Records](./DNS-Records.png)

## Configuracion de nginx para redireccionar el trafico

```bash
# Instalar nginx, certbot y los otros paquetes necesarios
sudo apt install nginx
sudo apt install unzip
sudo apt install net-tools
sudo snap install certbot --classic
sudo snap install node --classic

# 1) Es importante que el dominio a certificar apunte a la maquina que esta creando el certificado.
# 2) El puerto 80 debe estar permitido por firewall
# 3) Esta operacion es interactiva.
sudo certbot --nginx -d 'api.arquitecturaccp.com' -d 'www.api.arquitecturaccp.com'

sudo vim /etc/nginx/sites-available/default
```

---

```nginx
# /etc/nginx/sites-available/default

upstream prototoken {
    server 127.0.0.1:3000;
    keepalive 64;
}

server {
    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;
    server_name api.arquitecturaccp.com www.api.arquitecturaccp.com; # managed by Certbot

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;
    }

    location /create-token {
        proxy_pass http://prototoken/create-token;
    }

    location /ordencompra {
        auth_request /validate;
        proxy_pass https://app-service-cpp-001.azurewebsites.net/ordencompra;
    }

    location /transporte {
        auth_request /validate;
        proxy_pass https://app-service-ccp-002.azurewebsites.net/transporte;
    }

    #location /consultaruta/[0-9]+ {
    #    auth_request /validate;
    #    proxy_pass https://app-service-ccp-003.azurewebsites.net/consultaruta/;
    #}

    location /estadoordencompra {
        auth_request /validate;
        proxy_pass https://app-service-cpp-003.azurewebsites.net/estadoordencompra;
    }

    location = /validate {
        internal;
        proxy_pass              http://prototoken/validate;
        proxy_pass_request_body off;
        proxy_set_header        Content-Length "";
        proxy_set_header        X-Original-URI $request_uri;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/api.arquitecturaccp.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/api.arquitecturaccp.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
    if ($host = www.api.arquitecturaccp.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = api.arquitecturaccp.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80 ;
    listen [::]:80 ;
    server_name api.arquitecturaccp.com www.api.arquitecturaccp.com;
    return 404; # managed by Certbot
}

```

---

```bash
sudo systemctl restart nginx
```
