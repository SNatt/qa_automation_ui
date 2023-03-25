from locators.auth_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def auth_forms_fill(self, email, password):
        self.element_is_visible(self.locators.CHOOSE_LOGIN).click()
        self.element_is_visible(self.locators.REMEMBER).click()
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SUBMIT).click()

    def sign_up_forms_fill(self, firstname, lastname, email, password, conf_password):
        self.element_is_visible(self.locators.SIGN_UP_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(lastname)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.CONFIRM_PASSWORD).send_keys(conf_password)
        self.element_is_visible(self.locators.REGISTER_BUTTON).click()



    def sign_up_checking_positive(self):
        res = self.element_is_present(self.locators.REG_CHECKING_POSITIVE).text
        return res

    def sign_up_checking_negative(self):
        res = self.element_is_present(self.locators.REG_CHECKING_NEGATIVE).text
        return res

    def control_visit_lk(self):
        res = self.element_is_present(self.locators.FULL_USER_NAME).text
        return res

    def check_mistakes_auth_form(self):
        res = self.element_is_present(self.locators.CHECK_LOGIN).text
        return res
