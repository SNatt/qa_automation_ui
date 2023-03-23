from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Заполняемые поля
    EMAIL = (By.CSS_SELECTOR, "input[id='username']")