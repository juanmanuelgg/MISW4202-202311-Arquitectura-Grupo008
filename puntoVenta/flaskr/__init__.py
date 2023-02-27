from flask import Flask 
from .modelos import db,  PuntoVentaShema

punto_venta_schema = PuntoVentaShema()


def create_app(config_name):
    app = Flask(__name__)  
    # conn = get_db_connection()
    db_url = "postgresql://ccpdbuser001:project-1234@ccp-postgresql.postgres.database.azure.com:5432/orden_compra"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False
    return app
