import allure
from selene import browser, have
import requests


class AddProduct:

    @allure.story('Добавление товара через api')
    def add_product(self, id_product):
        url = 'https://demowebshop.tricentis.com/addproducttocart/details/'
        with allure.step('Отправка запроса с указанным id товара'):
            response = requests.post(url + id_product)
        with allure.step('Проверка кода'):
            assert response.status_code == 200
        with allure.step('Получение cookie'):
            self.cookie = response.cookies.get('Nop.customer')

        return self

    @allure.story('Открытие корзины')
    def open_cart(self):
        with allure.step('Открытие браузера'):
            browser.open('')
        with allure.step('Добавление cookie'):
            browser.driver.add_cookie({"name": "Nop.customer", "value": self.cookie})
        with allure.step('Перезагрузка браузера'):
            browser.driver.refresh()

        return self

    @allure.story('Проверка товаров в корзине')
    def check_add_product(self, name_product):
        with allure.step('Проверка имени товара'):
            browser.element('.product-name').should(have.text(name_product))

        return self

    @allure.story('Проверка количества товаров в корзине')
    def check_qty_product(self, quantity):
        with allure.step('Проверка количества товара'):
            from selene import have
            browser.element('.qty-input').should(have.value(quantity))

        return self

    @allure.step('Проверка цены товара')
    def check_price_of_good(self, price):
        browser.element('.product-unit-price').should(have.exact_text(price))

add_product_api = AddProduct()