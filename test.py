from fastapi.testclient import TestClient
from main import app

fake_db = []

client = TestClient(app)


