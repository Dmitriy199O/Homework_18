from flask import Flask
from flask_restx import Api
from app.config import Config
from app.create_db import db
from app.load_data import load_data
from app.views.movies import movies_ns
from app.views.director import director_ns
from app.views.genres import genre_ns

def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def configure_app(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app_config = Config()
app = create_app(app_config)
configure_app(app)

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()
