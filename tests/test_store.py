import pytest
from pets_store_tests.test_data.store import place_order
from pets_store_tests.pages.store_page import StorePage
from pets_store_tests.app.models import Order


class TestStore:
    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.store_page = StorePage(base_url)

    def test_place_order(self):
        response = self.store_page.place_order(place_order)
        assert response.status_code == 200
        order = self.store_page.validate(Order, response)
        assert order.id == 1
        assert order.status == "placed"

    def test_find_purchase_order_by_id(self):
        response = self.store_page.find_purchase(1)
        assert response.status_code == 200
        order = self.store_page.validate(Order, response)
        assert order.id == 1

    def test_delete_order(self):
        response = self.store_page.delete_order(1)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == '1'

    def test_get_inventory(self):
        response = self.store_page.get_inventory()
        assert response.status_code == 200
        inventory = response.json()
        assert isinstance(inventory, dict)
        for status, quantity in inventory.items():
            assert isinstance(status, str)
            assert isinstance(quantity, int)