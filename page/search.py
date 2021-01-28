from page.base import BasePage

class Search(BasePage):

    def search(self):
        self.run_dds("../page/search.yaml", "search")
        return True

