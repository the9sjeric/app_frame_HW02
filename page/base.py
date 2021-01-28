from selenium.webdriver.remote.webdriver import WebDriver
from appium.webdriver.common.mobileby import By
from handle_black.handle_black import HandleBlack
import yaml

class BasePage():

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @HandleBlack
    def find(self, byele):
        # black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_back']")]
        # try:
        #     return self.driver.find_element(*byele)
        # except Exception as err:
        #     for black in black_list:
        #         black_ele = self.driver.find_elements(*black)
        #         if len(black_ele) > 0:
        #             black_ele[0].click()
        #             return self.find(byele)
        #     raise err
        return  self.driver.find_element(*byele)

    def find_click(self, byele):
        return self.find(byele).click()

    def find_send(self, byele, text):
        return self.find(byele).send_keys(text)

    def find_get_text(self, byele):
        return self.find(byele).text

    def run_dds(self, data_path, action):
        with open(data_path, 'r', encoding="utf-8") as f:
            yamldata = yaml.safe_load(f)
        dds = yamldata[action]
        for dd in dds:
            operation = dd['action']
            if operation == 'find_click':
                self.find_click(dd['location'])
            elif operation == 'find_send':
                self.find_send(dd['location'], dd['text'])


