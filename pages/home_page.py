from playwright.async_api import Page
from pages.base_page import BasePage
from locators.locators import Locators as l
from utils.urls import Urls
from utils.config_manager import ConfigManager
from utils.browser_manager import ensure_page_is_initialized

class HomePage(BasePage):
    def __init__(self, page:Page, config:ConfigManager):
        super().__init__(page, config)

    @ensure_page_is_initialized
    async def open(self):
        await self.page.goto(Urls.homepage)
