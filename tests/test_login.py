import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("admin", "password")
    assert page.is_result_displayed()
    assert "Успешно! Вход выполнен." in page.get_result_text()

def test_invalid_login(browser):
    page = LoginPage(browser)
    page.open()
    page.login("wrong_user", "password")
    assert page.is_result_displayed()
    assert "Ошибка: Неверный логин или пароль." in page.get_result_text()

def test_invalid_password(browser):
    page = LoginPage(browser)
    page.open()
    page.login("admin", "wrong_pass")
    assert page.is_result_displayed()
    assert "Ошибка: Неверный логин или пароль." in page.get_result_text()
