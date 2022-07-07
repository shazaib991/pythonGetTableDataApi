# ENDPOINTS
# Get request at "http://localhost:5000/api/v1/tableData" expect to recieve table data in json format

from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

url = "https://www.govcagecodes.com/?code=&company=TESLA#results"

try:
    tableHeaders = []

    source = requests.get(url).text

    soup = BeautifulSoup(source, "lxml")
    table = soup.find("table", id="rt")

    for td in table.thead.tr.find_all("td"):
        tableHeaders.append(td.text)

    df = pd.DataFrame(columns=tableHeaders)

    for tr in table.tbody.find_all("tr"):
        data = tr.find_all("td")
        tableRows = [td.text for td in data]
        length = len(df)
        df.loc[length] = tableRows

    df.to_json("./tableData.json")
except Exception as err:
    print(err)

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
