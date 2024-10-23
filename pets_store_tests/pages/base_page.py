class BasePage:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def validate(model, response):
        return model(**response.json())