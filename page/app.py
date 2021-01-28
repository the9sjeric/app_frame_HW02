from appium import webdriver
from page.base import BasePage
from page.main import MainPage
from time import sleep

class App(BasePage):

    def start_app(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": "true"
            }
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def stop_app(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        sleep(5)
        return MainPage(self.driver)