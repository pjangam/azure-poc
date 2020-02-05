from flask import Flask, request
from myazure.aks import AksClient, AksConfig
import logging
import uuid

logging.basicConfig(format='%(levelname)s:%(message)s    %(asctime)s ', datefmt='%m/%d/%Y %I:%M:%S %p')
app = Flask(__name__)
aksClient = AksClient()



# class Controller:
#    def __init__(self):
#        pass

@app.route("/")
def get_help():
    return "TBD help page"


@app.route("/clusters/<resource_group>/<cluster_name>", methods=["POST"])
def create_cluster(resource_group, cluster_name):
    rid = uuid.uuid4()
    logging.debug(f"received {rid} create: {resource_group}/{cluster_name}")

    body = request.get_json()
    body["resource_group"] = resource_group
    body["cluster_name"] = cluster_name
    aks_config = AksConfig(body)
    status = aksClient.create(aks_config)

    logging.debug(f"complete {rid} create: {resource_group}/{cluster_name}")

    return status


@app.route("/clusters/<resource_group>/<cluster_name>", methods=["DELETE"])
def delete_cluster(resource_group, cluster_name):
    status = aksClient.delete(resource_group, cluster_name)
    return status
