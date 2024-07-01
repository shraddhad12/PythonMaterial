#pip install pytest
#pip install pytest-mock

# You need to install a suitable plugin for your async framework, for example:
#     - anyio
#     - pytest-asyncio
#     - pytest-tornasync
#     - pytest-trio
#     - pytest-twisted

import pytest
from fastapi.testclient import TestClient
from main import app, get_data

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_get_data(mocker):
    mock_data = {"data": "mocked data"}
    mocker.patch("main.get_data", return_value=mock_data)

@pytest.mark.asyncio
async def test_read_data(client, mocker):
    mock_data = {"data": "mocked async data"}
    mocker.patch("main.get_data", return_value=mock_data)
    response = await client.get("/async-data")
    assert response.status_code == 200
    assert response.json() == mock_data