from selenium.webdriver.common.by import By

class Locators:
    LOGO = By.XPATH, ".//*[@id='root']/div/header/nav/div/a"  # Логотип сайта
    TITLE_FILLING = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']" # Заголовок "Начинки" в меню
    TITLE_SAUCE = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']" # Заголовок "Соусы" в меню
    TITLE_BUNS = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']" # Заголовок "Булки" в меню
    SPAN_SAUCES = By.XPATH, ".//span[text()='Соусы']/parent::*"   # Кнопка "Соусы" в меню
    SPAN_FILLING = By.XPATH, ".//span[text()='Начинки']/parent::*"  # Кнопка "Начинки" в меню
    SPAN_BUNS = By.XPATH, ".//span[text()='Булки']/parent::*"  # Кнопка "Булки" в меню
    INPUT_EMAIL = By.XPATH, ".//label[text() = 'Email']/following-sibling::input"  # Поле ввода email пользователя
    INPUT_PASSWORD = By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input"  # Поле ввода пароля пользователя
    BUTTON_LOGIN = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти" в форме входа в ЛК
    BUTTON_LK = By.XPATH, './/p[text()="Личный Кабинет"]'  # Kнопка "Личный кабинет" в шапке
    PROFILE_LINK = By.XPATH, './/a[text()="Профиль"]'  # Ссылка "Профиль" в ЛК
    BUTTON_CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]'  # Kнопка "Конструктор" в шапке
    BUTTON_LOGOUT = By.XPATH, './/button[text()="Выход"]'  # Kнопка "Выход" из личного кабинета
    BUTTON_ORDER = By.XPATH, './/button[text()="Оформить заказ"]'  # Kнопка "Оформить заказ" на основной странице после авторизации
    LINK_PASS_RECOVERY = By.XPATH, './/a[text()="Восстановить пароль"]'  # Ссылка "Восстановить пароль"
    BUTTON_PASS_RECOVERY = By.XPATH, './/button[text()="Восстановить"]'  # Кнопка "Восстановить пароль"
    LINK_LOGIN_PASS_RECOVERY = By.XPATH, './/a[text()="Войти"]'  # Ссылка в форме восстановления пароля - "Войти"
    BUTTON_REG = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    INPUT_USER_NAME = By.XPATH, ".//label[text() = 'Имя']/following-sibling::input"  # Поле ввода имени пользователя
    TEXT_PASSWORD_WRONG = By.XPATH, './/p[text() = "Некорректный пароль"]'  # Текст "Некорректный пароль"
    BUTTON_ENTER_LK = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт" на главной

