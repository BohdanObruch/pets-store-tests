import pytest
import os
from dotenv import load_dotenv

from pets_store_tests.utils.requests_helper import set_base_url

load_dotenv()

@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env", default="PROD")
    url = os.getenv("DEV") if env == "DEV" else os.getenv("PROD")
    set_base_url(url, env)
    return url

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="PROD", help="Environment to run tests against")

