import pytest
from page.app import App



class TestAddMember():

    def setup(self):
        self.app = App()
        self.main = self.app.start_app().goto_main()

    def teardown(self):
        self.app.stop_app()

    def test_search(self):
        result = self.main.goto_quotation().goto_search().search()
        assert result