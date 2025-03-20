import asyncio
from playwright.async_api import async_playwright, Browser, BrowserContext, Page, Playwright
from utils.config_manager import config_manager
from functools import wraps


def ensure_playwright_initialized(func):
    """Decorator to check if Playwright is initialized before running the function."""
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if self.playwright is None:
            raise RuntimeError("Playwright is not initialized. Call 'start()' first.")
        return await func(self, *args, **kwargs)
    return wrapper

def ensure_page_is_initialized(func):
    """Decorator to check if Page is initialized before running the function."""
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if self.page is None:
            raise RuntimeError("Page is not initialized. Call BrowserManager 'start()' first.")
        return await func(self, *args, **kwargs)
    return wrapper

class BrowserManager:
    def __init__(self):
        self.config = config_manager
        self.playwright: Playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser: Browser = await self.playwright.chromium.launch(
                headless=self.config.headless
                )
        self.context: BrowserContext = await self.browser.new_context(
                accept_downloads=self.config.accept_downloads
                )
        self.page: Page = await self.context.new_page()
    
    @ensure_playwright_initialized
    async def close(self):
        await self.browser.close()
        await self.playwright.stop()


