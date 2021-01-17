from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from .base import BasePage


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)
        # locators
        self.username_loc = (By.ID, 'input-username')
        self.password_loc = (By.ID, 'input-password')
        self.login_loc = (By.XPATH, "//button[@class='btn btn-primary']")
        self.logout_loc = (By.XPATH, "//a[contains(@href,'logout&user_token')]")
        self.catalog_loc = (By.XPATH, "//i[@class='fa fa-tags fw']")
        self.sales_loc = (By.XPATH, "//i[@class='fa fa-shopping-cart fw']")
        self.developer_settings_loc = (By.XPATH, "//div[@class='container-fluid']/div[@class='pull-right']")
        self.title_loc = (By.XPATH, "//h4[@class='modal-title']")


    def _set_username_(self, name):
        self.find_element(locator=self.username_loc).clear()
        self.find_element(locator=self.username_loc).send_keys(name)

    def _set_password_(self, password):
        self.find_element(locator=self.password_loc).clear()
        self.find_element(locator=self.password_loc).send_keys(password)

    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.login_loc).click()

    def logout(self):
        self.find_element(locator=self.logout_loc).click()

    def click_catalog(self):
        el = self.find_element(self.catalog_loc)
        self.actions.click(el).perform()

    def click_sales(self):
        el = self.find_element(self.sales_loc)
        self.actions.click(el).perform()

    def click_developer_settings(self):
        el = self.find_element(self.developer_settings_loc)
        self.actions.click(el).perform()


