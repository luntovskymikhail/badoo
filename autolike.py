from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import ExcelFunctions
import openpyxl

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.maximize_window()

#opens main page
driver.get("https://badoo.com/")

#click login button
driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div/a').click()

#enters log and pass
driver.find_element_by_name("email").send_keys(input("EnterPhone: "))
driver.find_element_by_name("password").send_keys(input("EnterPassword: "))

#click enter button
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button').click()

#opens search range page
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="app_s"]/div/div/div/div[1]/div/div[3]/div/div').click()

#change search range
slider = driver.find_element_by_xpath('//*[@id="search_form"]/div/fieldset[3]/div/div/div/div/div[2]')
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(30, 0).release().perform()
driver.find_element_by_xpath('//*[@id="search_form"]/div/div[2]/div/div[1]/div').click()
time.sleep(4)

#click like button
driver.implicitly_wait(30)
driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()

#click skip browser announcemnets button
driver.implicitly_wait(20)
driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div').click()

#infinity loop for likes
while True:
    path = "C://Users//Mikhail//PycharmProjects//badoo//count.xlsx"
    # write result at next column
    book = openpyxl.load_workbook(path)
    sheet = book.active

    driver.implicitly_wait(20)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]').click()
    num = sheet.max_column + 1
    ExcelFunctions.writeData(path, "List1", 1, num, "Liked")