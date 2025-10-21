from faker import Faker

faker = Faker()

class PlayerLocalization:

    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            "nickname": self.fake.first_name()
        }

    def build(self):
        return self.result

    def set_number(self, number=11):
        self.result['number'] = number
        return self