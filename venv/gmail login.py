from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


chromedriver = 'D:\Documents\coding\chromedriver.exe'
browser = webdriver.Chrome(ChromeDriverManager().install())

#apparently the old code stopped supporting in 2018
#browser.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin','_blank')")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
           'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
           '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
driver.implicitly_wait(15)

loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys('sabrinacheung1029@gmail.com')
#from this onwards doens't work as chrome deemed driver not secure enough to proceed
nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()

passWordBox = driver.find_element_by_xpath(
    '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys(passWord)

nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()
