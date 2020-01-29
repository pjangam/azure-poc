import os

from flask import Flask, request
from myazure.aks import get_aks

app = Flask(__name__)


@app.route("/")
def getHelp():
    return "TBD help page"


@app.route("/createcluster", methods=["POST"])
def createCluster():
    body = request.get_json()
    print(body)
    aks = get_aks("a", "Standard_D2s_v3")
    aks.test1(body)
    return "Hello, World!"
