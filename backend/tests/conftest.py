import pytest
from fastapi.testclient import TestClient
from backend import app 

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)
