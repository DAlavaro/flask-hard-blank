# app

from flask import Flask
from flask_restx import Api
from config import Config
# from models import Review, Book
from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns

"""функция создания основного объекта app"""
def create_app(config: Config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    #register_extensions(app)
    return app

def configure_app(app: Flask):
    db.init_app(app)
    api = Api(app)

#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
# def register_extensions(app):
#     db.init_app(app)
#     api = Api(app)
#     api.add_namespace(...)
#     create_data(app, db)
#
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run(host="localhost", port=10001, debug=True)
