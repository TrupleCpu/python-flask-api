from flask import Flask
from flask_restful import Api
from models import db
from controller import LibraryResource, LibraryListResource

#using mysql instead of sql lite
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/databasename'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(LibraryListResource, '/api/library')
api.add_resource(LibraryResource, '/api/library/<string:isbn>')

if __name__ == '__main__':
    app.run(debug=True)