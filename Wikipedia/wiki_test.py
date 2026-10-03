from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto("https://www.wikipedia.org")

    page.locator("#searchInput").fill("QA")
    page.get_by_role("button", name="Search").click()

    expect(page).to_have_url("https://ru.wikipedia.org/wiki/QA")
