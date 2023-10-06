import yaml
from testpage import OperationsHelper
import time
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['login']
password = testdata['password']

def test_step1(browser):
    logging.info("Test 1 starting (UI)")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(1)
    testpage.enter_login(login)
    time.sleep(1)
    testpage.enter_pass(password)
    time.sleep(1)
    testpage.click_login_btn()
    time.sleep(1)
    testpage.click_about_btn()
    time.sleep(1)
    assert testpage.get_header_size() == "32px"