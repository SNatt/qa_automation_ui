from pages.auth_page import TextBoxPage
from config import base_url, valid_email, valid_password



class TestElements:
    class TestTextBox:
        def test_RTKM_001(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_positive())
            assert text_box_page.sign_up_checking_positive() == 'Подтверждение email'

        def test_RTKM_002(self, driver):
            firstname = 'Ivan'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

        def test_RTKM_003(self, driver):
            firstname = 'Иван98'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

        def test_RTKM_004(self, driver):
            firstname = 'Иванреостыклрьорагцуфбдщнотвсми'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


        def test_RTKM_005(self,driver):
            firstname = 'Иван'
            lastname = 'Ivanov'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

        def test_RTKM_006(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов131'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

        def test_RTKM_007(self, driver):
            firstname = 'Иван'
            lastname = 'Ивановхщьбюавстерытсдекйоьбвтмп'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

        def test_RTKM_008(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'иван_иванов@майл.ком'
            password = 'Qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

        def test_RTKM_009(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwer'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwer')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Длина пароля должна быть не менее 8 символов'

        def test_RTKM_010(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'qwertyui98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='qwertyui98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Пароль должен содержать хотя бы одну заглавную букву'

        def test_RTKM_011(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'йцукенгш98'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='йцукенгш98')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Пароль должен содержать только латинские буквы'

        def test_RTKM_012(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwerty'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password='Qwerty')
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Длина пароля должна быть не менее 8 символов'

        def test_RTKM_013(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98ghbnuyjmdjh'
            conf_password = 'Qwertyui98ghbnuyjmdjh'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password)
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Длина пароля должна быть не более 20 символов'

        def test_RTKM_014(self, driver):
            firstname = 'Иван'
            lastname = 'Иванов'
            email = 'ivan_ivanov@mail.com'
            password = 'Qwertyui98'
            conf_password = 'Qwertyui99'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.sign_up_forms_fill(firstname, lastname, email, password, conf_password)
            print(text_box_page.sign_up_checking_negative())
            assert text_box_page.sign_up_checking_negative() == 'Пароли не совпадают'

        def test_RTKM_015(self, driver):
            email = valid_email
            password = valid_password
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.auth_forms_fill(email, password)
            print(text_box_page.control_visit_lk())
            assert text_box_page.control_visit_lk() == 'Иванов\nИван'

        def test_RTKM_016(self, driver):
            email = 'ivan_ivanov@mail.com'
            password = valid_password
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.auth_forms_fill(email, password)
            print(text_box_page.check_mistakes_auth_form())
            assert text_box_page.check_mistakes_auth_form() == 'Неверный логин или пароль'

        def test_RTKM_017(self, driver):
            email = valid_email
            password = 'Qwertyui9876'
            url = base_url
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            text_box_page.auth_forms_fill(email, password)
            print(text_box_page.check_mistakes_auth_form())
            assert text_box_page.check_mistakes_auth_form() == 'Неверный логин или пароль'