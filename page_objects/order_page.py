import allure

from selenium.webdriver.common.keys import Keys

from page_objects.base_page import BasePage
from locators.order_page_locators import OrderLocators

class OrderPage(BasePage):

    @allure.step('Ожидание загрузки страницы заказа')
    def wait_load_order_page(self):
        self.wait_for_element_visibility(OrderLocators.NEXT_BUTTON)

    @allure.step('Заполнение поля Имя')
    def user_name(self, name):
        self.fill_fields(OrderLocators.NAME, name)

    @allure.step('Заполнение поля Фамилия')
    def user_lastname(self, lastname):
        self.fill_fields(OrderLocators.LAST_NAME, lastname)

    @allure.step('Заполнение поля Адрес')
    def user_address(self, address):
        self.fill_fields(OrderLocators.ADDRESS, address)

    @allure.step('Заполнение поля Станция метро')
    def user_metro(self, metro):
        self.fill_fields(OrderLocators.METRO, metro)
        self.wait_element_to_be_clickable(OrderLocators.CHOSEN_STATION)
        self.click_element(OrderLocators.CHOSEN_STATION)

    @allure.step('Заполнение поля Телефон')
    def user_phone_number(self, number):
        self.fill_fields(OrderLocators.PHONE_NUMBER, number)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Загрузка второй страницы заказа')
    def wait_load_second_order_page(self):
        self.wait_for_element_visibility(OrderLocators.ORDER_BUTTON_ON_ORDER_PAGE)

    @allure.step('Выбор даты заказа')
    def order_date(self, order_date):
        self.fill_fields(OrderLocators.DELIVERY_DATE, order_date + Keys.ENTER)

    @allure.step('Выбор срока заказа')
    def order_rent_time(self, days):
        self.click_element(OrderLocators.RENT_TIME)
        select_rent_time=OrderLocators.rent_time_locator(days)
        self.wait_element_to_be_clickable(select_rent_time)
        self.click_element(select_rent_time)

    @allure.step('Выбор цвета самоката')
    def scooter_color(self, color):
        colors={
                'чёрный жемчуг': OrderLocators.BLACK_SCOOTER_COLOR,
                'серая безысходность': OrderLocators.GREY_SCOOTER_COLOR,
        }
        self.click_element(colors[color])

    @allure.step('Заполнение поля Комментарий для курьера')
    def comment_for_courier(self, comment):
        self.fill_fields(OrderLocators.ORDER_COMMENT, comment)

    @allure.step('Нажатие кнопки "Заказать"')
    def click_order_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON_ON_ORDER_PAGE)

    @allure.step('Ожидание загрузки окна подтверждения заказа')
    def wait_load_confirm_window(self):
        self.wait_element_to_be_clickable(OrderLocators.YES_BUTTON)

    @allure.step('Нажатие кнопки подтверждения заказа')
    def click_confirm_button(self):
        self.click_element(OrderLocators.YES_BUTTON)

    @allure.step('Ожидание загрузки окна с информацией о заказе')
    def wait_load_order_number_window(self):
        self.wait_for_element_visibility(OrderLocators.ORDER_COMPLETED)

    @allure.step('Полный позитивный сценарий заказа самоката')
    def make_order(self, name, lastname, address, metro, number, order_date, days, color, comment):
        self.wait_load_order_page()
        self.user_name(name)
        self.user_lastname(lastname)
        self.user_address(address)
        self.user_metro(metro)
        self.user_phone_number(number)
        self.click_next_button()
        self.wait_load_second_order_page()
        self.order_date(order_date)
        self.order_rent_time(days)
        self.scooter_color(color)
        self.comment_for_courier(comment)
        self.click_order_button()
        self.wait_load_confirm_window()
        self.click_confirm_button()
