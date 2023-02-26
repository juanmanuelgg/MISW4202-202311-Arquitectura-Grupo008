from flask import Flask

def create_app(config_name):
    app = Flask(__name__)  
    db_url = 'postgresql://ccpdbuser001:project-1234@ccp-postgresql.postgres.database.azure.com:5432/transporte'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app