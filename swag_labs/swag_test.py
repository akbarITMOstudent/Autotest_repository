from playwright.sync_api import Page, expect

#def test_login(page: Page):
#    page.goto("https://www.saucedemo.com") ## run to page
#
#    print("URL:", page.url)
#    print("TITLE:", page.title())
#    
#    page.get_by_placeholder("Username").fill("standard_user")
#    page.get_by_placeholder("Password").fill("secret_sauce")
#
#    page.get_by_role("button", name="Login").click() #Go to page
#
#    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_ui(page: Page):
    page.goto("https://www.saucedemo.com")

    #expect(page).to_have_screenshot("homepage.png")

    if page.get_by_placeholder("Username").is_enabled():
        page.get_by_placeholder("Username").fill("standard_user")
    if page.get_by_placeholder("Password").is_enabled():
        page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    box = page.locator(".inventory_item_img").nth(1).bounding_box()
    print(box)
    assert box is not None, "Picture not found on page"
    assert box["width"] > 0 and box["height"] > 0, "Picture size equals 0" 

    box = page.locator(".add-to-cart-sauce-labs-backpack").nth(2).bounding_box()
    print(box)
    assert box is not None, "button is bot found in page"
    assert box["width"] > 0 and box["height"] > 0, "Button size equals 0"

    page.get_by_role("button", name="add-to-cart-sauce-labs-backpack").click()

