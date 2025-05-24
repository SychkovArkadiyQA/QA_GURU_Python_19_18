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


add_product_api = AddProduct()