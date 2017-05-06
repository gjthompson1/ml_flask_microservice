from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from lib import seniority

import time

seniority.initialize_models()

app = Flask(__name__)
api = Api(app)

class Seniority(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('job_title', type=str, help='Job title cannot be converted')
        parser.add_argument('type', type=str, help='Option cannot be converted')
        args = parser.parse_args()

        _option = args.get('type')

        if _option == 'probability':
            prediction = seniority.predict_one_proba(args['job_title'])
        else:
            prediction = seniority.predit_one_abs(args['job_title'])

        return prediction

api.add_resource(Seniority, '/seniority')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0',debug=True)
