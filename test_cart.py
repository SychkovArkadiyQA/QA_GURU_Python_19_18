from unittest import result
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
from selene.support.conditions import have
import allure

from pages.cart_page import add_product_api
from pages.auth import auth

from data.data import ID_PRODUCT_1, NAME_1


@allure.story('Авторизация через API')
@allure.story('Добавление и проверка товара в корзине')
def test_add_product():
    with allure.step('Авторизация через API'):
        auth.login_api()
    with allure.step('Добавление и проверка товара в корзине'):
        (add_product_api.add_product(ID_PRODUCT_1).open_cart().check_add_product(NAME_1))





