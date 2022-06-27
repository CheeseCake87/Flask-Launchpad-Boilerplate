from flask import session

from flask_launchpad import FLBlueprint

fl_bp = FLBlueprint()
bp = fl_bp.register()

fl_bp.import_routes("routes")

structure = fl_bp.config["structure"]


@bp.before_app_first_request
def before_app_first_request():
    pass


@bp.before_app_request
def before_app_request():
    for key in fl_bp.session:
        if key not in session:
            session.update(fl_bp.session)
            break


@bp.after_app_request
def after_app_request(response):
    return response
