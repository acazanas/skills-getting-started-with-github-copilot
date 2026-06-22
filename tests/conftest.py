import importlib
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def reset_app_module():
    import src.app as app_module
    importlib.reload(app_module)
    yield


@pytest.fixture
def client():
    from src.app import app
    return TestClient(app)
