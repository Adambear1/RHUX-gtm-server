from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from main import Website

app = Flask(__name__, template_folder='templates')
api = Api(app)
CORS(app)

api.add_resource(Website, "/api/website", methods=["GET", "POST", "PUT"])

if __name__ == "__main__":
    app.run(debug=True)