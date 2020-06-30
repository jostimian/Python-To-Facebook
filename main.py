from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

email = input("Enter Your Email: ")
password = input("Enter Your Password")

def login():
    browser = webdriver.Chrome()
    browser.get("https://www.facebook.com")

    emailid = browser.find_element_by_id("email")
    passid = browser.find_element_by_id("pass")
    loginid = browser.find_element_by_id("loginbutton")

    emailid.send_keys(email)
    passid.send_keys(password)
    loginid.click()


while email or password == "":
    print("\n")
    email = input("Enter Your Email: ")
    password = input("Enter Your Password")
    if email and password != "":
        login()

if email and password != "":
    login()
