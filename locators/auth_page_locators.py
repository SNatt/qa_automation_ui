from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Данные для входа
    EMAIL = (By.CSS_SELECTOR, "input[id='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    REMEMBER = (By.CSS_SELECTOR, "span[class='rt-checkbox__label']")
    CHOOSE_LOGIN = (By.CSS_SELECTOR, "div[id='t-btn-tab-mail']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='kc-login']")

    # Данные для регистрации
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "a[id='kc-register'")
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[id='address']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[id='password-confirm']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='register']")

    # Подтверждение регистрации (для позитивных сценариев)
    REG_CHECKING_POSITIVE = (By.CSS_SELECTOR, "h1[class='card-container__title']")

    # Локатор для негативных сценариев (форма регистрации нового пользователя)
    REG_CHECKING_NEGATIVE = (By.CSS_SELECTOR, "span[class='rt-input-container__meta rt-input-container__meta--error']")

    # Локаторы личного кабинета
    FULL_USER_NAME = (By.CSS_SELECTOR, "h2[title='Иванов Иван']")

    # Локаторы ошибок формы авторизации
    CHECK_LOGIN = (By.CSS_SELECTOR, "span[id='form-error-message']")


