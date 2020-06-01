#python selenium demo

#import what I need
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

#set my driver object
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()

#go to facebook.com
driver.get("https://facebook.com/")

#make browser full screen
driver.maximize_window()

#type the email in the email field
email_field = driver.find_element_by_id("email")
email_field.send_keys("testemail123@gmail.com")
time.sleep(3)

#type the password in the password field
pss_field = driver.find_element_by_id("pass")
pss_field.send_keys("testpassword")
time.sleep(3)

#click the login button
login_button = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_id("u_0_b"))
login_button.click()

#find all the text on the screen
body = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//*[@id='facebook']/body/div[2]"))

time.sleep(10)

all_text = body.text

#verify the error message is displayed
if "Sorry, something went wrong." not in all_text:
   raise BaseException("The 'Sorry, something went wrong.' text is not found.")
else:
   print("Test Passed")
    
time.sleep(20)

driver.quit()

