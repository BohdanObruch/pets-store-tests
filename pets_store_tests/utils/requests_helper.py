from pets_store_tests.utils.attach import response_logging, response_attaching
import requests
from typing import Optional

base_url: Optional[str] = None
env_name: Optional[str] = None

def set_base_url(url, env):
    global base_url, env_name
    base_url = url
    env_name = env

def api_request(endpoint, method, **kwargs):
    url = f"{base_url}{endpoint}"
    response = requests.request(method, url, **kwargs)
    response_logging(response, base_url, env_name)
    response_attaching(response, base_url, env_name)
    return response