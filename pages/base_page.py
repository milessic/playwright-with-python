import asyncio
from playwright.async_api import Page
from utils.browser_manager import ensure_page_is_initialized
from utils.config_manager import ConfigManager
from utils.pathutils import get_filename_index
from locators.locators import Locators as l

class BasePage():
    def __init__(self, page, config):
        self.page:Page = page
        self.config = config
    
    @ensure_page_is_initialized
    async def verify_that_topnav_is_visible(self):
        await self.wait_until_element_is_visible(l.CommonLocators.topnav)

    @ensure_page_is_initialized
    async def click(self, locator):
        await self.page.click(locator)

    @ensure_page_is_initialized
    async def wait_and_click(self, selector: str):
        await self.wait_until_element_is_visible(selector)
        await self.page.click(selector)

    @ensure_page_is_initialized
    async def fill_text(self, selector: str, text: str):
        await self.page.fill(selector, text)
    
    @ensure_page_is_initialized
    async def wait_until_element_is_visible(self, selector, timeout: int | None = None):
        await self.page.wait_for_selector(selector, state="visible", timeout=self.config.timeout if timeout is None else timeout)
    
    @ensure_page_is_initialized
    async def take_screenshot(self, screenshot_name:str="screenshot-{index}.png", full_page:bool=True, **kwargs):
        r"""If ``{index}`` is provided, then it adds index number rather than overriding exsiting file."""
        filepath = get_filename_index(self.config.screenshot_path + screenshot_name).removesuffix(".png").removesuffix(".jpg") + ".jpg"
        return await self.page.screenshot(
                path=filepath,
                full_page=full_page,
                **kwargs
                )

