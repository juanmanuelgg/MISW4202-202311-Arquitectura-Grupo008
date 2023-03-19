from flask import Flask
import psycopg2
import os
from .modelos import db,  OrdenDeCompraSchema

orden_compra_schema= OrdenDeCompraSchema()

def get_db_connection():
    conn = psycopg2.connect(host='ccp-postgresql.postgres.database.azure.com',
                            database='orden_compra',
                            user=os.environ['ccpdbuser001'],
                            password=os.environ['project-1234'])
    return conn

def create_app(config_name):
    app = Flask(__name__)  
    # conn = get_db_connection()
    
    db_url = "postgresql://ccpdbuser001:project-1234@ccp-postgresql.postgres.database.azure.com:5432/orden_compra"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "frase-secreta"
    return app