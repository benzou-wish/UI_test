import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


"""https://github.com/SergeyPirogov/webdriver_manager"""
# turn off webdriver_manager log
# import logging
# logging.getLogger('WDM').setLevel(logging.NOTSET)


# open browser
# firefox
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager(path=r'./drivers').install()))
# driver.get(r'https://www.google.com')
# search_box = driver.find_element(by=By.NAME, value=r'q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

# use ChromeDriverService to control driver start and stop
service = Service(ChromeDriverManager(path=r'./drivers').install())
service.start()
driver = webdriver.Remote(command_executor=service.service_url,
                          options=None)
driver.get(r'https://www.google.com')
search_box = driver.find_element(by=By.NAME, value=r'q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()