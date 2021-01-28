from page.base import BasePage
from page.quotation import Quotation
from appium.webdriver.common.mobileby import By


class MainPage(BasePage):
    def goto_quotation(self):
        self.run_dds("../page/main.yaml", "goto_quotation_page")
        # self.find_click((By.XPATH, '//*[contains(@resource-id,"tab_name") and @text="行情"]'))
        return Quotation(self.driver)

    # 手动制造黑名单页面
    def goto_blacklist(self):
        self.driver.find_element(By.XPATH, '//*[contains(@resource-id,"action_message")]').click()
        return self

    def goto_workspace(self):
        pass

    def goto_mypage(self):
        pass