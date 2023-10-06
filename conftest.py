import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def browser(scope="session"):
   service = Service(executable_path='/bin/chromedriver')
   options = webdriver.ChromeOptions()
   driver = webdriver.Chrome(service=service, options=options)
   yield driver
   driver.quit()
