import tomllib
import logging

from logging import Logger
from selenium.webdriver.remote.webdriver import WebDriver 
from typing import Dict, Any
from login import LinkedInLoginBot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
import webdriver_manager.chrome as chrome_driver_manager


SETTINGS_TOML_FILEPATH = 'data/config.toml'

def load_settings_dict(filepath) -> Dict[str, Any]:
    with open(filepath, 'rb') as file:
        return tomllib.load(file)
    
class LinkedInBot:
    # components
    options: ChromeOptions
    logger: Logger
    browser: WebDriver
    login_bot: LinkedInLoginBot
    
    # settings
    email: str
    password: str
    
    def __init__(self, settings_dict: Dict[str, Any]):
        self._initialize_settings_fields(settings_dict)
        self._set_chrome_options()
        self._initialize_browser()
        self._initialize_logger()
        self._initialize_linkedin_login_bot()
        
    def _initialize_settings_fields(self, settings_dict: Dict[str, Any]):
        self.email = settings_dict["login-info"]["email"]
        self.password = settings_dict["login-info"]["password"]

    def _set_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.options = options

    def _initialize_browser(self):
        chrome_service = ChromeService(chrome_driver_manager().install())
        self.browser = webdriver.Chrome(service=chrome_service, options=self.options)

    def _initialize_logger(self):
        self.logger = logging.getLogger(__name__)
        
    def _initialize_linkedin_login_bot(self):
        self.login_bot = LinkedInLoginBot(self.browser, self.logger, self.email, self.password)

    def start_login_loop(self):
        self.login_bot.start_linkedin()

if __name__ == "__main__":
    settings = load_settings_dict(SETTINGS_TOML_FILEPATH)
    bot = LinkedInBot(settings)
    bot.start_login_loop()