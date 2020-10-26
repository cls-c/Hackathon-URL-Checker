#require Selenium Webdriver-manager (to automatic install chrome)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://urlchecker-dev-ed.lightning.force.com/lightning/page/home')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("sabrinacheung1029@gmail.com")
password.send_keys("S@Brina3516")

browser.find_element_by_name("Login").click()
#this is the new tab function:
#try:
    #lement = WebDriverWait(browser, 10).until(
   #     EC.presence_of_element_located((By.ID, "wrap"))
   # )
#finally:
   #browser.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin','_blank')").click()


#Comment: Was having trouble logging into the gmail, because gmail stopped supporting automation
# Will be working on a second script, but able to use and open new tab
#email=browser.find_element_class_name("Xb9hP")
#email.send_keys("sabrinacheung1029@gmail.com")
#browser.find_element_by_class_name("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc").click()\
