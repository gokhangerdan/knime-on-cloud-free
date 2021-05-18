from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

import pandas as pd
import knime

knime.executable_path = "app/knime_4.1.0/knime"

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

class KnimeDocker(Resource):
    def post(self):
        with knime.Workflow("app/knimepy") as wf:
            wf.execute()
            output_table = wf.data_table_outputs[0]

        return output_table.to_json()

api.add_resource(KnimeDocker, '/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
