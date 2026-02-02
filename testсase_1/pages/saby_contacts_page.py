'''
1)Перейти на https://saby.ru в раздел "Контакты" (Ещё <> офисов в
регионе).
2) Найти баннер Тензор, кликнуть по нему
3) Перейти на https://tensor.ru/
4) Проверить, что есть блок "Сила в людях"
5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
https://tensor.ru/about
6) Находим раздел Работаем и проверяем, что у всех фотографии
хронологии одинаковые высота (height) и ширина (width)
'''

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SabyContactsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    