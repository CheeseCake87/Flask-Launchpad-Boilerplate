from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_launchpad import FlaskLaunchpad
from flask_launchpad import FLStructure
from flask_launchpad import Security


fl = FlaskLaunchpad()
db = SQLAlchemy()
structures = FLStructure()
security = Security()


def create_app():
    main = Flask(__name__)
    fl.init_app(main)
    fl.app_config("app_config.toml")

    security.init_app(main)

    fl.models_folder("models")
    db.init_app(main)

    structures.init_app(main, "structures")
    structures.register_structure("bootstrap")

    fl.import_builtins("flask/routes")
    fl.import_builtins("flask/template_filters")

    fl.import_apis("api")
    fl.import_blueprints("blueprints")

    return main
