import os

import requests
from dotenv import load_dotenv

load_dotenv()


def test_mlflow_server():
    """Test if mlflow server is running."""
    req = requests.get(os.getenv("MLFLOW_TRACKING_URI"))

    assert req.status_code == 401
