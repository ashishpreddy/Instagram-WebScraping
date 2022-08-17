import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Creates the object that interacts with google chrome
# Replace the double stars with the path for your chromedriver
driver = webdriver.Chrome(executable_path="**")
driver.get("https://www.instagram.com/accounts/login/")

# the login information of the account
user_name = "***"
password = "**"

# logs into the account by sending the information to the webpage
time.sleep(0.2)
element = driver.find_elements_by_class_name("f0n8F ")
element[0].send_keys(user_name)
element[0].send_keys(Keys.ENTER)

time.sleep(0.2)
element[1].send_keys(password)
element[1].send_keys(Keys.ENTER)

# clicks through the pop up messages
time.sleep(4.5)
element = driver.find_element_by_class_name("cmbtv").click()
time.sleep(2)
element = driver.find_element_by_class_name("mt3GC").click()

# enters your account and opens the following
time.sleep(0.5)
#Replace the double stars with your account name
element = driver.find_element_by_link_text("**").click()
time.sleep(1.5)
element = driver.find_element_by_partial_link_text("following").click()

# scrolls to the bottom of the pop up window; approximated the necessary time after a True while loop
time.sleep(4)
pop_up = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
t0 = time.time()
t1 = time.time()
while (t1 - t0) < 360:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
      pop_up)
    t1 = time.time()

# Finds the list of the followers
elements = driver.find_elements_by_xpath("//a[@class = 'FPmhX notranslate  _0imsa ']")
followers = ["hello"]
for ele in elements:
    followers.append(ele.get_attribute("title"))
followers.pop(0)

# Use to validate the web scraping
print("The length of your elements are", len(elements))
print("The length of the followers array is", len(followers))
print("\nThe first follower of yours is", followers[0])

# closes the pop-up window to move onto the following pop-up
element = driver.find_element_by_xpath("//div[@class= 'WaOAr']/button[@class = 'wpO6b  ']")
driver.execute_script("arguments[0].click();", element)

# opens the followers pop-up window
time.sleep(1.5)
element = driver.find_element_by_partial_link_text("followers").click()

# scrolls to the bottom of the pop-up window
time.sleep(4)
pop_up = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
t0 = time.time()
t1 = time.time()
while (t1 - t0) < 360:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
      pop_up)
    t1 = time.time()

# finds the list of people you are following
elements = driver.find_elements_by_xpath("//a[@class = 'FPmhX notranslate  _0imsa ']")
following = ["hello"]
for ele in elements:
    following.append(ele.get_attribute("title"))
following.pop(0)

# Used to validate the results
print("The length of your elements are", len(elements))
print("The length of the following array is", len(followers))
print("\nThe first person you are following is", followers[0])
