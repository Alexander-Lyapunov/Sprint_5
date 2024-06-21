# Сервис для тестирования - [Stella Burgers](https://stellarburgers.nomoreparties.site/) 

## Тестировались следующие функции (все тесты содержатся в директории tests):
### Раздел «Конструктор» - test_constructor.py
### Выход из аккаунта - test_logout.py
### Переход из личного кабинета в конструктор  - test_go_to_constructor.py
### Переход в личный кабинет - test_go_to_lk.py
### Вход - test_login.py
### Регистрация - test_registration.py

### url использующиеся в проекте хранятся в файле urls.py в директории data
### Данные для входа в личный кабинет хранятся в файле data.py в директории data
### Рандомайзеры для тестов содержатся в файле helpers.py
### Локаторы для выполнения тестов распологаются в файле locators.py

### Запустить все тесты 
```shell
pytest tests/
```