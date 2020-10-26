
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

chromedriver = 'D:\Documents\coding\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://mindful-unicorn-ic5494-dev-ed.lightning.force.com/lightning/n/trlhdtips__Welcome')

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("cheuklamsabrina.cheung@mindful-unicorn-ic5494.com")
password.send_keys("P@ssword123")

browser.find_element_by_name("Login").click()