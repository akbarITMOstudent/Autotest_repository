from playwright.sync_api import Page, expect

def test_login(page: Page):
    for attempt in range(3):
        page.goto("https://www.crunchyroll.com")
        page.wait_for_timeout(2000)

        if "/premium/error" in page.url:
            print(f"Попытка {attempt + 1}: сайт вернул ошибку, пробуем снова")
            continue
        else:
            break

    # если после всех попыток всё равно ошибка — тест сам явно упадёт тут
    assert "/premium/error" not in page.url, "Crunchyroll стабильно отдаёт страницу ошибки"

    try:
        page.get_by_role("button", name="Продолжить").wait_for(state="visible", timeout=3000)
        page.get_by_role("button", name="Продолжить").click()
    except Exception:
        pass

    try:
        page.get_by_role("button", name="Согласиться").wait_for(state="visible", timeout=3000)
        page.get_by_role("button", name="Согласиться").click()
    except Exception:
        pass

    page.get_by_role("button", name="ВОЙТИ").click()
    page.get_by_label("Email").fill("djinyuichi@gmail.com")
    page.get_by_label("Пароль").fill("")
    page.get_by_role("button", name="ВОЙТИ").click()

    expect(page).to_have_url("https://www.crunchyroll.com/ru/discover")