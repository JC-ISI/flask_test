from flask import Blueprint, Response, request
bp_obj1 = Blueprint("test_bp1", __name__)

@bp_obj1.route("/api/v1/test", methods=['GET'])
def hello():
    return "Welcome to pathfactory"