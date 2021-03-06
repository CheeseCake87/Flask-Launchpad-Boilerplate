from flask import session

from flask_launchpad import FLBlueprint

fl_bp = FLBlueprint()
bp = fl_bp.register()
structure = fl_bp.config['settings']["structure"]

fl_bp.import_routes("routes")


@bp.before_request
def before_request():
    for key in fl_bp.session:
        if key not in session:
            session.update(fl_bp.session)
            break


@bp.after_request
def after_request(response):
    return response
