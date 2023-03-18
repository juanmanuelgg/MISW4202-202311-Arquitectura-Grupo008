#!/bin/bash

# USER_API_GATEWAY es secreto y el archivo .pem debe ir el el .gitignore
ssh -i API-Gateway_key.pem ${USER_API_GATEWAY}@api.arquitecturaccp.com