import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visibility(self, locator):
        WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))

    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание кликабельности элемента')
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable(locator))

    @allure.step('Заполнение поля')
    def fill_fields(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Получение адреса текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
