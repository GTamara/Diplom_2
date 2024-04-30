import datetime
import random
import string


class SharedHelperFuncs:

    @staticmethod
    def generate_random_string(length: int) -> str:
        letters = string.ascii_lowercase + string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def generate_password(self, length: int) -> str:
        return self.generate_random_string(length)

    def generate_random_email(self, length: int) -> str:
        return self.generate_random_string(length) + '@yandex.ru'

    def get_ingredients_list(self, ingredients_obj: dict[str, list]):
        return list(
            map(
                lambda item: item['_id'], ingredients_obj
            )
        )