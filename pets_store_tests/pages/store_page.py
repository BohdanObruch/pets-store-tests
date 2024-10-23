from pets_store_tests.pages.base_page import BasePage
from pets_store_tests.utils.requests_helper import api_request


class StorePage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/store"

    def place_order(self, place_order):
        response = api_request(f"{self.endpoint}/order", "POST", json=place_order)
        return response

    def find_purchase(self, oder_id):
        response = api_request(f"{self.endpoint}/order/{oder_id}", "GET")
        return response

    def delete_order(self, oder_id):
        response = api_request(f"{self.endpoint}/order/{oder_id}", "DELETE")
        return response

    def get_inventory(self):
        response = api_request(f"{self.endpoint}/inventory", "GET")
        return response
