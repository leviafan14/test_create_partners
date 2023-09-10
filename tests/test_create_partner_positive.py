import pytest
import time
from playwright.sync_api import Page, expect
from playwright.sync_api import Playwright
from auth_data import *
from data_for_testing import *


# Авторизация перед выполнением тестов
@pytest.fixture(scope="session")
def partner_page(playwright: Playwright) -> Page:
    # Открытие окна бразуера
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Переход на страницу авторизации
    page.goto(admin_auth_page)
    # Ввод номера телефона
    page.locator("[placeholder=\"Телефон\"]").fill(login)
    # Ввод пароля
    page.locator("[placeholder=\"Пароль\"]").fill(password)
    # Нажатие на кнопку "Войти"
    page.locator("text=Войти").click()
    return page


# Открытие страницы создания партнера
def test_open_create_partner_page(partner_page: object) -> None:
    time.sleep(3)
    partner_page.goto("https://dev.admin.domka.shop/partners")
    with partner_page.expect_navigation(url=create_partner_page):
        partner_page.get_by_role("link", name="Добавить").click()


# Создание партнера ИП. ИНН: 12 цифр