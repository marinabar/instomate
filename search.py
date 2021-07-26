from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys


def setupsel():

    # Set up profile
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/home/mrnb/Bureau/code/Profile")
    browser = webdriver.Chrome("/home/mrnb/Bureau/code/2020/instomate/chromedriver", chrome_options=options)# Specify path to driver

    return browser

def geturl(url):

    browser = setupsel()
    # Wait so that the pop up doesn't? appear and then load
    browser.implicitly_wait(5)
    browser.get(url)
    return browser# Get url

def searchimg(word, N):

    word += " site:pinterest.com" # Specify searching site

    # browser = setupsel()
    browser = geturl("https://www.google.com")

    # Get search bar xPath
    search = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search.send_keys(word,Keys.ENTER) # Search for query

    # Find images
    link = browser.find_element_by_link_text("Images")
    link.get_attribute("href")
    link.click()

    # Create directory for saved images
    try:
        os.mkdir("saved")
    except FileExistsError:
        pass

    browser.implicitly_wait(3)

    # Loop and download images
    elements = browser.find_elements_by_class_name('rg_i')

    count = 0
    for e in range(len(elements)):
        # get images source url
        elements[e].click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')
        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
            big_img = element[1].find_element_by_class_name('n3VNCb')
        
        # Get source and then download
        src = big_img.get_attribute("src")
        urllib.request.urlretrieve(src, os.path.join('saved','image'+str(e)+'.jpg'))
        count +=1
        if count == N:
                break
    
    browser.quit()