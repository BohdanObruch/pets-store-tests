from pets_store_tests.pages.base_page import BasePage
from pets_store_tests.utils.requests_helper import api_request


class UserPage(BasePage):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.endpoint = "/user"

    def create_users_with_array(self, users_data):
        response = api_request(f"{self.endpoint}/createWithArray", "POST", json=users_data)
        return response

    def create_users_with_list(self, users_data):
        response = api_request(f"{self.endpoint}/createWithList", "POST", json=users_data)
        return response

    def get_user_by_username(self, username):
        response = api_request(f"{self.endpoint}/{username}", "GET")
        return response

    def update_user(self, username, user_data):
        response = api_request(f"{self.endpoint}/{username}", "PUT", json=user_data)
        return response

    def delete_user(self, username):
        response = api_request(f"{self.endpoint}/{username}", "DELETE")
        return response

    def login_user(self, username, password):
        response = api_request(f"{self.endpoint}/login", "GET", params={"username": username, "password": password})
        return response

    def logout_user(self):
        response = api_request(f"{self.endpoint}/logout", "GET")
        return response

    def create_user(self, user_data):
        response = api_request(self.endpoint, "POST", json=user_data)
        return response
