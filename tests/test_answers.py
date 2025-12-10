import allure
import pytest

from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators

from data import FAQAnswers

class TestAnswers:

    @allure.title('Проверка ответов на вопросы в блоке FAQ')
    @pytest.mark.parametrize('index, expected_answer', FAQAnswers.ANSWERS)
    def test_check_answers_in_faq(self, driver, index, expected_answer):
        allure.dynamic.description(f'Проверяем, что при нажатии на вопрос {index} открывается ответ с нужным текстом')
        main_page = MainPage(driver)
        main_page.wait_load_main_page()
        main_page.click_accept_cookie_button()
        main_page.scroll_to_questions()
        main_page.click_faq_question(index)
        main_page.wait_for_element_visibility(MainPageLocators.answer_locator(index))
        assert main_page.get_answer_text(index) == expected_answer
