import pytest

from application.webservice.api.server import launch


@pytest.fixture
def client():
    app = launch()
    with app.test_client() as client:
        yield client