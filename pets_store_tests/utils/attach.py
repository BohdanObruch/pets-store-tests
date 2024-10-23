import allure
import logging
import json
from requests import Response
from allure_commons.types import AttachmentType

def response_logging(response: Response, base_url: str, env_name: str):
    request_url = response.request.url.replace(base_url, env_name)
    logging.info("Request: " + request_url)
    if response.request.body:
        if isinstance(response.request.body, bytes):
            logging.info("INFO Request body: " + response.request.body.decode('utf-8'))
        else:
            logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)

def response_attaching(response: Response, base_url: str, env_name: str):
    request_url = response.request.url.replace(base_url, env_name)
    allure.attach(
        body=request_url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=response.request.method,
        name="Method",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.request.headers),
        name="Request headers",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.status_code),
        name="Response code",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        if isinstance(response.request.body, bytes):
            allure.attach(
                body=response.request.body.decode('utf-8', errors='replace'),
                name="Request body",
                attachment_type=AttachmentType.TEXT,
            )
        else:
            allure.attach(
                body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
                name="Request body",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="Response",
        attachment_type=AttachmentType.JSON,
        extension="json",
    )