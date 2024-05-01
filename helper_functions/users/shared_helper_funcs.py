import random
import string

import allure


class SharedHelperFuncs:

    @staticmethod
    @allure.step('Сгенерировать случайную строку')
    def generate_random_string(length: int) -> str:
        letters = string.ascii_lowercase + string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def generate_password(self, length: int) -> str:
        return self.generate_random_string(length)

    def generate_random_email(self, length: int) -> str:
        return self.generate_random_string(length) + '@yandex.ru'

    @staticmethod
    @allure.step('Получить список ингредиентов')
    def get_ingredients_list(ingredients_obj: dict[str, list]):
        return list(
            map(
                lambda item: item['_id'], ingredients_obj
            )
        )
