from pets_store_tests.pages.base_page import BasePage
from pets_store_tests.utils.requests_helper import api_request
from pets_store_tests.utils.resource import path


class PetPage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/pet"

    def add_pet(self, pet_data):
        response = api_request(self.endpoint, "POST", json=pet_data)
        return response

    def update_pet(self, pet_data):
        response = api_request(self.endpoint, "PUT", json=pet_data)
        return response

    def get_pet_by_id(self, pet_id):
        response = api_request(f"{self.endpoint}/{pet_id}", "GET")
        return response

    def delete_pet(self, pet_id):
        response = api_request(f"{self.endpoint}/{pet_id}", "DELETE")
        return response

    def find_pets_by_status(self, status):
        response = api_request(f"{self.endpoint}/findByStatus", "GET", params={"status": status})
        return response

    def find_pets_by_tags(self, tags):
        response = api_request(f"{self.endpoint}/findByTags", "GET", params={"tags": tags})
        return response

    def upload_image(self, pet_id, image):
        response = api_request(f"{self.endpoint}/{pet_id}/uploadImage", "POST", files={"file": open(path(image), "rb")})
        return response
