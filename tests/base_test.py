from pages.base_page import BasePage
from pages.home_page import HomePage

async def test_open_mj_portfolio_page(browser_manager):
    base_page = BasePage(browser_manager.page, browser_manager.config)
    home_page = HomePage(browser_manager.page, browser_manager.config)
    await home_page.open()
    await base_page.take_screenshot("homepage-{epoch}-{index}")

