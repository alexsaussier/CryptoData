from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep
from datetime import datetime

browser = webdriver.Firefox(executable_path='C:\\Users\\Alexandre\\Programming\\Python Programs\\geckodriver.exe')

i = 1

# The amount of different cryptos we want to get data from
while i < 100:
    browser.get('https://www.coingecko.com/fr')
    sleep(5)

    # Click on the crypto from main menu
    crypto = browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]"
                                          "/div/div/table/tbody/tr[" + str(i) + "]/td[3]/div/div[2]/a[1]")
    crypto.click()

    # Click on Historical Data tab.
    historical_data = browser.find_element_by_xpath('//*[@id="navigationTab"]/li[4]/a').click()

    sleep(7)

    # Gather data starting 2010-01-01
    click_date = browser.find_element_by_xpath('/html/body/div[4]/div[6]/div/'
                                               'div[2]/div/div/div[2]/div[2]/input[1]').click()

    for j in range(11):
        scroll_2010 = browser.find_element_by_xpath('/html/body/div[10]/div[1]/div/div/div/span[2]').click()
    sleep(7)

    # Click on Jan 1st
    jan_1st = browser.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[2]/div/span[7]')

    # Download CSV file
    export_to_format = browser.find_element_by_xpath('/html/body/div[4]/div[6]/'
                                                     'div/div[2]/div/div/div[3]/button').click()
    sleep(5)
    download = browser.find_element_by_xpath('/html/body/div[4]/div[6]/div/div[2]/div/div/div[3]/ul/li[2]/a').click()

    i += 1

    sleep(5)

