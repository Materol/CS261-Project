# May have to use pip3 install --user selenium
# May have to use pip3 install --user pyvirtualdisplay
from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

display = Display(visible=0, size=(800,600))
display.start()

browser = webdriver.Chrome(executable_path=r'./chromedriver')

browser.get("https://mango-dune-07a8b7110.1.azurestaticapps.net/?repo=Materol%2FChess-Engine")

try:
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[xmlns='http://www.w3.org/2000/svg']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

html = browser.find_element(By.CSS_SELECTOR, "*[xmlns='http://www.w3.org/2000/svg']").get_attribute('outerHTML')

with open("./project.svg", "w") as file:
    file.write(html)

browser.quit()
display.stop()