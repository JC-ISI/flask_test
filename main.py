import json

from flask import Flask, request, Response
# from apis.media import media_api
# from apis.users import users_api
# from apis.adtc import adtc_api
# from apis.pcr import ocr_api
# from apis.celery import celery_api
# from apis.dashboard import dashboard_api
from flask_cors import CORS
from api.v1.sample_1 import bp_obj
from api.v1.sample_2 import bp_obj1

# # from error_handlers import error_blueprint (to integrate error handlers if needed)
#
app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/*": {
#     "origins": ["http://xerox.tatrasdata.com.s3-website.ap-south-1.amazonaws.com", "http://localhost:4200",
#                 "http://13.161.174.41:4200", "http://13.161.174.44:4200"]}})
app.register_blueprint(bp_obj)
app.register_blueprint(bp_obj1)
# app.register_blueprint(adtc_api)
# app.register_blueprint(ocr_api)
# app.register_blueprint(celery_api)
# app.register_blueprint(dashboard_api)




# @app.route("/home", methods=['GET'])
# def hello():
#     return "Welcome to Xerox"
# @app.route("/test", methods=['GET'])
# def hello_():
#     return "Welcome to PF"


if __name__ == "__main__":
    # Only for debugging while developing

    app.run(host='0.0.0.0', debug=True)


