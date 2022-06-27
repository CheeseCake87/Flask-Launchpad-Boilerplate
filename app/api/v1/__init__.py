from flask_restx import Api
from flask import session

from flask_launchpad import FLBlueprint

fl_bp = FLBlueprint()

api_bp = fl_bp.register()
api = Api(api_bp, doc=f"/docs")

fl_bp.import_routes()


@api_bp.before_app_first_request
def before_app_first_request():
    pass


@api_bp.before_app_request
def before_app_request():
    for key in fl_bp.session:
        if key not in session:
            session.update(fl_bp.session)
            break


@api_bp.after_app_request
def after_app_request(response):
    return response
