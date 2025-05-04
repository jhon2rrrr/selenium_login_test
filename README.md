UI-тесты

Сайт для тестирования: https://berpress.github.io/selenium-login-demo/

Реализовано 3 автотеста:
Успешный вход с корректными данными
Ошибка при неверном логине
Ошибка при неверном пароле

Как запустить*

1. Клонировать проект: git clone https://github.com/jhon2rrrr/selenium_login_test.git
2. Перейти в папку: cd selenium_login_test
3. Установить зависимости: pip install -r requirements.txt
(Если выдаст ошибку следовать пунктам 3.1-3.4, если нет то сразу к 4 пункту)
3.1* (Если выдаст ошибку с) Скачать виртуальное окружение: sudo apt install python3-venv
3.2* Создать виртуальое окружение: python3 -m venv venv
3.3* Активировать: source venv/bin/activate
3.4* Заново установить зависимость: pip install -r requirements.txt
4. Установить Google Chrome: wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
5. Установить ChromeDriver: sudo apt install chromium-chromedriver
6. Запустить тесты: pytest
