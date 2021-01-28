from page.base import BasePage
from appium.webdriver.common.mobileby import By

class Market(BasePage):

    def addfrom_wechat(self):
        pass

    def addfrom_phone(self):
        pass

    def addfrom_manual(self):
        pass

    def check_page(self):
        ele = self.find_get_text((By.XPATH, '//*[contains(@resource-id,"index_name") and @text="上证指数"]'))
        return ele
