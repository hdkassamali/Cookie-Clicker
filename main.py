import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/hadikassamali/Development/chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60*5


store_items = driver.find_elements(By.CSS_SELECTOR, "div #store b")
item_list = [item.text.split("-")[0].rstrip(" ") for item in store_items[0:7]]
item_list.reverse()

while time.time() < timeout:
  buy_timer = time.time() + 13
  while time.time() < buy_timer:
    cookie.click()
  for item in item_list:
    buy_item = driver.find_element(By.ID, f"buy{item}")
    try:
      buy_item.click()
    except:
      pass
    else:
      time.sleep(0.01)
      buy_timer += 2

cookies_per_second = driver.find_element(By.ID, "cps")
print(cookies_per_second.text)