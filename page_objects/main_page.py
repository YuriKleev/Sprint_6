import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('Ожидание загрузки главной страницы')
    def wait_load_main_page(self):
        self.wait_for_element_visibility(MainPageLocators.question_locator('last()'))

    @allure.step('Нажатие на кнопку принятия куков')
    def click_accept_cookie_button(self):
        self.wait_element_to_be_clickable(MainPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_element(MainPageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" вверху страницы')
    def click_upper_order_button(self):
        self.click_element(MainPageLocators.UPPER_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать" внизу страницы')
    def click_lower_order_button(self):
        self.scroll_to_element(MainPageLocators.LOWER_ORDER_BUTTON)
        self.wait_element_to_be_clickable(MainPageLocators.LOWER_ORDER_BUTTON)
        self.click_element(MainPageLocators.LOWER_ORDER_BUTTON)

    @allure.step('Скролл до блока вопросов')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.question_locator(1))

    @allure.step('Нажатие на вопрос в блоке вопросов')
    def click_faq_question(self, index):
        question_locator=MainPageLocators.question_locator(index)
        self.wait_element_to_be_clickable(question_locator)
        self.click_element(question_locator)

    @allure.step('Получение текста ответа на вопрос в блоке вопросов')
    def get_answer_text(self, index):
        answer_locator=MainPageLocators.answer_locator(index)
        return self.find_element(answer_locator).text
