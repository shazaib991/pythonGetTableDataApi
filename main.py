# ENDPOINTS
# Get request at "localhost:5000/api/v1/getTableData" expect to recieve table data in json format

from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/api/v1/getTableData")
def getTableData():
    try:
        f = open("tableData.txt", "r")
        data = json.loads(f.read())
        f.close()

        return jsonify(data)
    except Exception as err:
        return jsonify({"error": f"{err}"}), 500


if __name__ == "__main__":
    app.run()
