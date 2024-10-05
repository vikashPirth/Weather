import os 
from selenium import webdriver


class Request:
    def __init__(self, base_url) -> None:
        self._phantomjs_path = os.path.join(os.curdir, 'phantomjs-2.1.1-macosx/bin/phantomjs')
        self._base_url = base_url
        self._driver = webdriver.PhantomJS(self._phantomjs_path)

    def fetch_data(self, forecast, area):
        url = self._base_url.format(forecast=forecast, area=area)
        self._driver.get(url)

        if self._driver.title == '404 Not Found':
            error_mesage = ('Could not find the area that you searching for ')
            raise Exception(error_mesage)
        
        return self._driver.page_source