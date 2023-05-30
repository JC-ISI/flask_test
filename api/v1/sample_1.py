import json
from flask import Blueprint, Response, request
bp_obj = Blueprint("test_bp", __name__)

@bp_obj.route("/api/v1/home", methods=['POST'])
def hello():
    data = request.get_json()
    if data['age'] > 50:
        msg = 'buro'
        sta = 200
    else:
        msg = 'kochi'
        sta = 400

    response_payload = {
        "message": msg
    }
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=sta)

# @bp_obj.route("/api/v1/test", methods=['GET'])
# def hello_pf():
#     return "Welcome to pf"