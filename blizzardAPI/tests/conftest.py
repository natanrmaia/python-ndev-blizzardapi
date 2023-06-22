import pytest
import os
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None)
    parser.addoption("--client", action="store", default=None)
    parser.addoption("--secret", action="store", default=None)
    parser.addoption("--region", action="store", default=None)
    parser.addoption("--locale", action="store", default=None)

@pytest.fixture
def token(request):
    return request.config.getoption("--token")

@pytest.fixture
def client(request):
    return request.config.getoption("--client")

@pytest.fixture
def secret(request):
    return request.config.getoption("--secret")

@pytest.fixture
def region(request):
    return request.config.getoption("--region")

@pytest.fixture
def locale(request):
    return request.config.getoption("--locale")

@pytest.fixture(autouse=True)
def setup():
    load_dotenv()

@pytest.fixture
def api_settings(client, secret, region, locale):

    return {
        'client_id': client or os.getenv('BLIZZARD_API_CLIENT_ID'),
        'client_secret': secret or os.getenv('BLIZZARD_API_CLIENT_SECRET'),
        'region': region or os.getenv('BLIZZARD_API_REGION'),
        'locale': locale or os.getenv('BLIZZARD_API_LOCALE')
    }