import os
import json
from flask import Flask, render_template
import requests


app = Flask(__name__)


# https://redcap.chop.edu/redcap_v9.3.4/index.php?pid=22810
redcap_token = os.environ.get("REDCAP_TOKEN_UGH")
assert len(redcap_token) == 32

post_parameters = {
    "token": redcap_token,
    "content": "record",
    "format": "json",
    "type": "flat",
    "rawOrLabel": "raw",
    "rawOrLabelHeaders": "raw",
    "exportCheckboxLabel": "false",
    "exportSurveyFields": "false",
    "exportDataAccessGroups": "false",
    "returnFormat": "json",
}


@app.route("/", methods=["GET"])
def home():
    r = requests.post("https://redcap.chop.edu/api/", data=post_parameters)
    issues = json.loads(r.content)
    return render_template("index.html", issues=issues)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
