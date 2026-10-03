import re
from playwright.sync_api import Page, expect

def test_add_to_basket_button(page: Page):
    page.goto("https://books.toscrape.com")

    page.get_by_role("link", name="Travel").click()
    expect(page).to_have_url(re.compile(r"/category/books/travel_2/"))
    expect(page.get_by_role("heading", name="Travel")).to_be_visible()

    first_book = page.locator("article.product_pod").first
    button = first_book.get_by_role("button", name="Add to basket")
    expect(button).to_be_visible()
    button.click()