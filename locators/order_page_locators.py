from selenium.webdriver.common.by import By

class OrderLocators():

    # Локаторы полей данных пользователя
    NAME=(By.XPATH, './/input[@placeholder="* Имя"]')
    LAST_NAME=(By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADDRESS=(By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO=(By.XPATH, './/input[@placeholder="* Станция метро"]')
    CHOSEN_STATION=(By.XPATH, './/li[@data-index="0"]')
    PHONE_NUMBER=(By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON=(By.XPATH, './/button[text()="Далее"]')

    # Локаторы полей данных об аренде
    DELIVERY_DATE=(By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    RENT_TIME=(By.XPATH, './/div[text()="* Срок аренды"]')

    @staticmethod
    def rent_time_locator(days):
        return (By.XPATH, f'.//div[text()="{days}"]')
    
    BLACK_SCOOTER_COLOR=(By.XPATH, './/label[@for="black"]')
    GREY_SCOOTER_COLOR=(By.XPATH, './/label[@for="grey"]')
    ORDER_COMMENT=(By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON_ON_ORDER_PAGE=(By.XPATH, './/button[contains(@class,"Button_Middle") and text()="Заказать"]')

    # Локатор кнопки Да во всплывающем окне подтверждения заказа
    YES_BUTTON=(By.XPATH, './/button[text()="Да"]')

    # Локатор текста в окне "Заказ оформлен"
    ORDER_COMPLETED=(By.XPATH, './/div[contains(text(), "Заказ оформлен")]')
