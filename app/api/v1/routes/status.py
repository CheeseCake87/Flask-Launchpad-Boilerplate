from flask_restx import Resource
from ..functions.api_auth import public_key_required

from .. import api


@api.route('/status')
class Test(Resource):
    def get(self):
        return "GET Method"

    def post(self, public_key):
        return """POST Method"""
