import pytest
from pets_store_tests.pages.pet_page import PetPage
from pets_store_tests.test_data.pet import add_pet, update_pet
from pets_store_tests.app.models import Pet


class TestPet:
    @pytest.fixture(autouse=True)
    def setup(self, base_url):
        self.pet_page = PetPage(base_url)

    def test_add_pet(self):
        response = self.pet_page.add_pet(add_pet)
        assert response.status_code == 200
        pet = self.pet_page.validate(Pet, response)
        assert pet.name == "Fluffy"
        assert pet.status == "available"

    def test_update_pet(self):
        response = self.pet_page.update_pet(update_pet)
        assert response.status_code == 200
        pet = self.pet_page.validate(Pet, response)
        assert pet.name == "Fluffy"
        assert pet.status == "sold"

    def test_get_pet_by_id(self):
        response = self.pet_page.get_pet_by_id(1)
        assert response.status_code == 200
        pet = self.pet_page.validate(Pet, response)
        assert pet.id == 1

    @pytest.mark.order("last")
    def test_delete_pet(self):
        response = self.pet_page.delete_pet(1)
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == "1"

    def test_find_pets_by_status(self):
        response = self.pet_page.find_pets_by_status("available")
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        for pet in pets:
            assert pet["status"] == "available"

    def test_find_pets_by_tags(self):
        response = self.pet_page.find_pets_by_tags("tag1,tag2")
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)
        for pet in pets:
            assert any(tag["name"] in ["tag1", "tag2"] for tag in pet["tags"])

    def test_upload_image(self):
        response = self.pet_page.upload_image(1, 'test.jpg')
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["code"] == 200
        assert json_response["type"] == "unknown"
        assert 'test.jpg' in json_response["message"]
