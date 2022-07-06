# ENDPOINTS
# Get request at "localhost:5000/api/v1/getTableData" expect to recieve table data in json format

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/getTableData")
def getTableData():
    try:
        return jsonify({"message": "this is a message to client"})
    except Exception as err:
        return jsonify({"error": f"{err}"}), 500


if __name__ == "__main__":
    app.run()
