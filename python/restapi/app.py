import os

from flask import Flask, request
from myazure.aks import AksClient, AksConfig

app = Flask(__name__)


@app.route("/")
def get_help():
    return "TBD help page"


@app.route("/createcluster", methods=["POST"])
def create_cluster():
    body = request.get_json()
    aks_config=AksConfig(body)
    aks = AksClient()
    status = aks.create(aks_config)
    return status
