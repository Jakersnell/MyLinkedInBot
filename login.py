from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from logging import Logger


class LinkedInLoginBot:
    LINKEDIN_LOG_IN_PAGE_URL = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"
    
    def __init__(self, browser: WebDriver, logger: Logger, email: str, password: str):
        self.browser = browser
        self.logger = logger
        self.email = email
        self.password = password

    def start_linkedin(self) -> None:
        self.logger.info("Logging in.....Please wait :)")
        self.browser.get(self.LINKEDIN_LOG_IN_PAGE_URL)
        try:
            email_field = self.browser.find_element("id", "username")
            password_field = self.browser.find_element("id", "password")
            login_button = self.browser.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
            email_field.send_keys(self.email)
            email_field.send_keys(Keys.TAB)
            time.sleep(2)
            password_field.send_keys(self.password)
            time.sleep(3)
            login_button.click()
            time.sleep(15)
        except TimeoutException:
            self.logger.info("TimeoutException! Username/password field or login button not found")
