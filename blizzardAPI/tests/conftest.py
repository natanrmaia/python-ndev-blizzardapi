import pytest
import os
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None)
    parser.addoption("--client", action="store", default=None)
    parser.addoption("--secret", action="store", default=None)
    parser.addoption("--region", action="store", default=None)
    parser.addoption("--locale", action="store", default=None)
    parser.addoption("--access_token", action="store", default=None)
    parser.addoption("--realm_id", action="store", default=None)
    parser.addoption("--character_id", action="store", default=None)
    parser.addoption("--realm_slug", action="store", default=None)
    parser.addoption("--character_name", action="store", default=None)
    parser.addoption("--season_id", action="store", default=None)
    parser.addoption("--bracket", action="store", default=None)
    parser.addoption("--guild_slug", action="store", default=None)


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

@pytest.fixture
def access_token(request):
    return request.config.getoption("--access_token")

@pytest.fixture
def realm_id(request):
    return request.config.getoption("--realm_id")

@pytest.fixture
def character_id(request):
    return request.config.getoption("--character_id")

@pytest.fixture
def realm_slug(request):
    return request.config.getoption("--realm_slug")

@pytest.fixture
def character_name(request):
    return request.config.getoption("--character_name")

@pytest.fixture
def season_id(request):
    return request.config.getoption("--season_id")

@pytest.fixture
def bracket(request):
    return request.config.getoption("--bracket")

@pytest.fixture
def guild_slug(request):
    return request.config.getoption("--guild_slug")

@pytest.fixture(autouse=True)
def setup():
    load_dotenv()


@pytest.fixture
def api_settings(client, secret, region, locale, access_token, realm_id, character_id, realm_slug, character_name, season_id, bracket, guild_slug):

    return {
        'client_id': client or os.getenv('BLIZZARD_API_CLIENT_ID'),
        'client_secret': secret or os.getenv('BLIZZARD_API_CLIENT_SECRET'),
        'region': region or os.getenv('BLIZZARD_API_REGION'),
        'locale': locale or os.getenv('BLIZZARD_API_LOCALE'),
        'access_token': access_token or os.getenv('BLIZZARD_API_ACCESS_TOKEN'),
        'realm_id': realm_id or os.getenv('BLIZZARD_API_REALM_ID'),
        'character_id': character_id or os.getenv('BLIZZARD_API_CHARACTER_ID'),
        'realm_slug': realm_slug or os.getenv('BLIZZARD_API_REALM_SLUG'),
        'character_name': character_name or os.getenv('BLIZZARD_API_CHARACTER_NAME'),
        'season_id': season_id or os.getenv('BLIZZARD_API_SEASON_ID'),
        'bracket': bracket or os.getenv('BLIZZARD_API_BRACKET'),
        'guild_slug': guild_slug or os.getenv('BLIZZARD_API_GUILD_SLUG')
    }