import json
import os

class ConfigManager:
    def __init__(self, config_file:str):
        try:
            c = json.load(open(config_file,"r"))
            self.environment = c["environment"]
        except FileNotFoundError:
            raise FileNotFoundError("FileNotFoundError: env.json file has not been found! Please refer to README.md how to create it.")
        except KeyError as e:
            raise KeyError(f"KeyError: Some of mandatory config keys have not been found! - {e}")
        self.headless = c.get("headless", True)
        self.accept_downloads = c.get("accept_downloads", False)
        self.timeout = c.get("timeout", 15)
        self.screenshot_path = c.get("screenshot_path", "TestOutput/")

# config_file_path should be located under root folder of the repository
config_file_name = "env.json"
config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_file_name)
config_manager = ConfigManager(config_file_path)

