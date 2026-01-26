from selenium.webdriver.common.by import By

class MainPageLocators():

    # Локаторы кнопок "Заказать" вверху и внизу главной страницы
    UPPER_ORDER_BUTTON=(By.XPATH, './/div[contains(@class,"Header")]/button[text()="Заказать"]')
    LOWER_ORDER_BUTTON=(By.XPATH, './/div[contains(@class,"FinishButton")]/button[text()="Заказать"]')

    # Локатор кнопки принятия куков
    ACCEPT_COOKIE_BUTTON=(By.XPATH, './/button[contains(@class,"App_CookieButton")]')

    # Локаторы лого Самоката и Яндекса
    LOGO_SCOOTER=(By.XPATH, './/a[@href="/"]')
    LOGO_YANDEX=(By.XPATH, './/a[@href="//yandex.ru"]')

    # Локаторы вопросов и ответов
    @staticmethod
    def question_locator(index):
        return (By.ID, f'accordion__heading-{index-1}')

    @staticmethod
    def answer_locator(index):
        return (By.ID, f'accordion__panel-{index-1}')

    # Локаторы подзаголовка главной страницы Самоката со словами "Самокат на пару дней"
    SCOOTER_SUBHEADER=(By.XPATH, './/div[contains(@class,"Home_Header")]')

    # Локатор хедера Дзена
    DZEN_HEADER=(By.ID, 'dzen-header')
