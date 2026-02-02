class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, *args):
        return self.driver.find_element(*args)

    def find_all(self, *args):
        return self.driver.find_elements(*args)
