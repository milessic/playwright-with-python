import pytest
from utils.browser_manager import BrowserManager

@pytest.fixture(scope="function")
async def browser_manager():
    manager = BrowserManager()
    await manager.start()
    yield manager
    await manager.close()

