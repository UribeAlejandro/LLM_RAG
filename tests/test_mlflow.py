import os

import requests


def test_mlflow_server():
    req = requests.get(os.getenv("MLFLOW_TRACKING_URI"))

    assert req.status_code == 200
