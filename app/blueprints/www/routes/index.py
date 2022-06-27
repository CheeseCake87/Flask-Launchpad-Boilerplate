from flask import render_template
from app import structures

from .. import bp
from .. import structure


@bp.route("/", methods=["GET"])
def index():
    render = "renders/structure-example.html"
    extend = structures.extend("main.html", structure)

    return render_template(render, extend=extend)
