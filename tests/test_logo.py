import allure

from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators

from url import *

class TestLogo:

    @allure.title('Проверка перехода на главную страницу "Самоката"')
    @allure.description('Проверяем, что при нажатии на лого "Самоката" происходит переход на главную страницу "Самоката"')
    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_upper_order_button()
        main_page.wait_element_to_be_clickable(MainPageLocators.LOGO_SCOOTER)
        main_page.click_element(MainPageLocators.LOGO_SCOOTER)
        assert main_page.wait_for_element_visibility(MainPageLocators.SCOOTER_SUBHEADER)

    @allure.title('Проверка редиректа на главную страницу "Дзена"')
    @allure.description('Проверяем, что при нажатии на лого "Яндекса" происходит редирект на главную страницу "Дзена"')
    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_element(MainPageLocators.LOGO_YANDEX)
        main_page.switch_to_new_window()
        assert main_page.wait_for_element_visibility(MainPageLocators.DZEN_HEADER)
