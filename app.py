# ENDPOINTS
# Get request at "http://localhost:5000/api/v1/tableData" expect to recieve table data in json format

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/v1/tableData")
def getTableData():
    try:
        f = open("./tableData.json", "r")
        data = json.loads(f.read())
        f.close()

        return jsonify(data)
    except Exception as err:
        return jsonify({"error": f"{err}"}), 500


if __name__ == "__main__":
    app.run()
