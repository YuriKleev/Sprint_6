import allure
import pytest

from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

from data import OrderData

class TestMakeOrder:

    @allure.title('Проверка позитивного сценария заказа самоката с двумя наборами данных и через разные точки входа')
    @pytest.mark.parametrize('order_button, order_info, button_location', 
        [
            [
                MainPageLocators.UPPER_ORDER_BUTTON,
                OrderData.ORDER_DATA_1,
                'верхнюю'
            ],
            [
                MainPageLocators.LOWER_ORDER_BUTTON,
                OrderData.ORDER_DATA_2,
                'нижнюю'
            ]
        ]
    )
    def test_place_order_success(self, driver, order_button, order_info, button_location):
        allure.dynamic.description(f'Проверяем позитивный сценарий через {button_location} кнопку Заказать')
        main_page=MainPage(driver)
        order_page=OrderPage(driver)
        main_page.click_accept_cookie_button()
        main_page.click_element(order_button)
        order_page.make_order(order_info['Name'], 
                              order_info['Last_name'], 
                              order_info['Address'], 
                              order_info['Metro'], 
                              order_info['Phone'], 
                              order_info['Date'], 
                              order_info['Rent_days'], 
                              order_info['Color'], 
                              order_info['Comment']
        )
        assert 'Заказ оформлен' in order_page.get_order_number_window_text()
