import pytest
from pets_store_tests.pages.user_page import UserPage
from pets_store_tests.test_data.user import create_user, update_user, users_list
from pets_store_tests.app.models import User


class TestUser:
    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.user_page = UserPage(base_url)

    def test_create_users_with_array(self):
        response = self.user_page.create_users_with_array(users_list)
        assert response.status_code == 200

    def test_create_users_with_list(self):
        response = self.user_page.create_users_with_list(users_list)
        assert response.status_code == 200

    def test_get_user_by_username(self):
        response = self.user_page.get_user_by_username("user1")
        assert response.status_code == 200
        user = self.user_page.validate(User, response)
        assert user.username == "user1"

    def test_update_user(self):
        response = self.user_page.update_user("user1", update_user)
        assert response.status_code == 200

    def test_delete_user(self):
        response = self.user_page.delete_user("user1")
        assert response.status_code == 200

    def test_login_user(self):
        response = self.user_page.login_user("user1", "password1")
        assert response.status_code == 200
        assert "X-Expires-After" in response.headers
        assert "X-Rate-Limit" in response.headers

    def test_logout_user(self):
        response = self.user_page.logout_user()
        assert response.status_code == 200

    def test_create_user(self):
        response = self.user_page.create_user(create_user)
        assert response.status_code == 200