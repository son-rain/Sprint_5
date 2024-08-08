from selenium.webdriver.common.by import By


class BurgerLocators:

    # Кнопка "Войти в аккаунт" на Главной
    HOME_LOGIN_BUTTON = (By.XPATH, '//button[contains(@class,"button") and text()="Войти в аккаунт"]')

    # Кнопка "Оформить заказ" на Главной
    HOME_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"button") and text()="Оформить заказ"]')

    # Ссылка на Личный кабинет на Главной
    HOME_ACCOUNT_BUTTON = (By.XPATH, '//a/p[text()="Личный Кабинет"]')

    # Надпись Собери бургер на Главной
    HOME_LABEL = (By.XPATH, '//div[@id="root"]//main//h1[text()="Соберите бургер"]')

    # Логотип
    HOME_LOGO = (By.XPATH, '//div[contains(@class, "logo")]/child::a')

    # Надпись Булки на Главной
    HOME_BUNS_LABEL = (By.XPATH, '//div[contains(@class,"Ingredients")]//h2[text()="Булки"]')

    # Надпись Начинки на Главной
    HOME_TOPPINGS_LABEL = (By.XPATH, '//div[contains(@class,"Ingredients")]//h2[text()="Начинки"]')

    # Раздел Булки на Главной
    HOME_BUNS_TAB = (By.XPATH, '//span[text()="Булки"]/parent::div[contains(@class,"tab")]')

    # Раздел Соусы на Главной
    HOME_SAUCES_TAB = (By.XPATH, '//span[text()="Соусы"]/parent::div[contains(@class,"tab")]')

    # Раздел Начинки на Главной
    HOME_TOPPINGS_TAB = (By.XPATH, '//span[text()="Начинки"]/parent::div[contains(@class,"tab")]')

    # Надпись Вход
    LOGIN_LABEL = (By.XPATH, '//div[contains(@class, "login")]/h2[text()="Вход"]')

    # Поле Email при входе
    LOGIN_NAME_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле Пароль при входе
    LOGIN_PWD_INPUT = (By.XPATH, '//form//input[@name="Пароль"]')

    # Кнопка Войти при входе
    LOGIN_ENTER_BUTTON = (By.XPATH, '//form[contains(@class,"Auth_form")]//button[text()="Войти"]')

    # Поле для ввода имени
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following::input[1]')

    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following::input[1]')

    # Поле для ввода пароля
    PWD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following::input[1]')

    # Кнопка выхода из профиля
    ACCOUNT_QUIT_BUTTON = (By.XPATH, '//li/button[text()="Выход"]')

    # Ссылка на профиль
    ACCOUNT_PROFILE_LINK = (By.XPATH, '//li/a[text()="Профиль"]')

    # Ссылка на вход со страницы восстановления пароля
    FORGOTTEN_PWD_LINK = (By.XPATH, '//main//div//a[text()="Войти"]')

    # Название страницы для восстановления пароля
    FORGOTTEN_LABEL = (By.XPATH, '//div[contains(@class, "login")]/h2[text()="Восстановление пароля"]')

    # Название страницы регистрации
    REGISTRATION_LABEL = (By.XPATH, '//div[contains(@class, "login")]/h2[text()="Регистрация"]')

    # Ссылка для входа со страницы регистрации
    REGISTRATION_LOGIN_LINK = (By.XPATH, '//main//div//a[text()="Войти"]')

    # Кнопка отправки формы регистрации
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, '//form[contains(@class, "Auth_form")]/button[text()="Зарегистрироваться"]')

    # Сообщения о неправильном вводе пароля
    REGISTRATION_PWD_ERR_LABEL = (By.XPATH, '//label[text()="Пароль"]/parent::div/following::p')

    # Переход в раздел конструктора
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')






