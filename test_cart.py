import allure

from pages.cart_page import add_product_api
from pages.auth import auth

from data.data import ID_PRODUCT_1, NAME_1, PRICE


@allure.story('Авторизация через API + Добавление и проверка товара в корзине')
def test_add_product():
    with allure.step('Авторизация через API'):
        auth.login_api()
    with allure.step('Добавление и проверка товара в корзине'):
        (add_product_api.add_product(ID_PRODUCT_1).open_cart().check_add_product(NAME_1))

@allure.story('Авторизация через API + Добавление и проверка количества товара в корзине')
def test_quantity_product():
    with allure.step('Авторизация через API'):
        auth.login_api()
    with allure.step('Добавление и проверка товара в корзине'):
        (add_product_api.add_product(ID_PRODUCT_1).open_cart().check_qty_product('1'))

@allure.story('Авторизация через API + Добавление и проверка цены товара в корзине')
def test_quantity_product():
    with allure.step('Авторизация через API'):
        auth.login_api()
    with allure.step('Добавление и проверка товара в корзине'):
        (add_product_api.add_product(ID_PRODUCT_1).open_cart().check_price_of_good(PRICE))





