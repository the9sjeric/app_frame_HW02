from appium.webdriver.common.mobileby import By

def HandleBlack(hdblack):
    def run(*args, **kwargs):
        black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_back']")]
        bypath = args[0]
        try:
            return hdblack(*args, **kwargs)
        except Exception as err:
            for black in black_list:
                black_ele = bypath.driver.find_elements(*black)
                if len(black_ele) > 0:
                    black_ele[0].click()
                    return hdblack(*args, **kwargs)
            raise err
    return run