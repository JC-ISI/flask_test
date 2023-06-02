import json
from flask import Blueprint, Response, request
from celery_task import add
bp_obj = Blueprint("test_bp", __name__)

@bp_obj.route("/api/v1/home", methods=['POST'])
def hello():
    data = request.get_json()
    x = data['x']
    y = data['y']
    task = add.apply_async((x,y))

    # if data['age'] > 50:
    #     msg = 'buro'
    #     sta = 200
    # else:
    #     msg = 'kochi'
    #     sta = 400

    response_payload = {
        "message": task.id
    }
    return Response(json.dumps(response_payload),
                    mimetype="application/json",
                    status=200)

# @bp_obj.route("/api/v1/test", methods=['GET'])
# def hello_pf():
#     return "Welcome to pf"