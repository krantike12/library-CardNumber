
import time
from argparse import Action
import imp
from lib2to3.pgen2 import driver
from time import time
from tracemalloc import stop
import webbrowser 
import json
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

f = open('member_details.json')



browser = webdriver.Chrome(options=chrome_options)

#openFile = open('memeber_details.json')

userid="krant"



browser.get("http://tclpstaff.bestbookbuddies.com")
    
browser.find_element_by_id('userid').send_keys(userid+"i") 
browser.find_element_by_id('password').send_keys("k1234")
browser.find_element_by_id('submit-button').click()


#For Searching Members
cardnumberprefix = 'MD-'
cardnumbersuffix = str(417)

browser.find_element_by_id('ui-id-4').click()
browser.find_element_by_id('searchmember').send_keys(cardnumberprefix+cardnumbersuffix)
 
#searchfield()

#browser.send_keys(keys.Enter).perform()

try:
		browser.find_element_by_xpath("//*[@id='patron_search']/form/input[3]").click()
except:
		browser.find_element_by_xpath("//*[@id='patron_search']/form/div[1]/input[3]").click()


# Editing the fields 
browser.find_element_by_xpath("//div[@id='patron-library-details']//a[@class='btn btn-default btn-xs'][normalize-space()='Edit']").click()

cardnumber= browser.find_element_by_id('cardnumber')

cardnumber.clear()
 
cardnumber.send_keys("MK-"+cardnumbersuffix)

browser.find_element_by_xpath("//button[@id='saverecord']").click()

#entredValue()




# print(editfield)

while cardnumbersuffix<str(420):
    browser.find_element_by_id('ui-id-1').click()
    browser.find_element_by_id('searchmember').send_keys(cardnumberprefix+cardnumbersuffix+str(1))
    try: 
        browser.find_element_by_xpath("//*[@id='patron_search']/form/input[3]").click()
    except: 
        browser.find_element_by_xpath("//*[@id='patron_search']/form/div[1]/input[3]").click()

browser.find_element_by_xpath("//div[@id='patron-library-details']//a[@class='btn btn-default btn-xs'][normalize-space()='Edit']").click()

cardnumber= browser.find_element_by_id('cardnumber')

cardnumber.clear()
 
cardnumber.send_keys("MK-"+cardnumbersuffix+str(1))

browser.find_element_by_xpath("//button[@id='saverecord']").click()
    

#to quit the window
# browser.quit()