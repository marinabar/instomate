from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

from search import setupsel, geturl # import set up function from previous file


def upload(mainword, N):

    des_words= """{mainword} 🌟/n
    what is your favorite outfit 1 - {N} ?

    tags ~
⠀
    #fashion #aesthetics #aestheticdress  #style #like #photography #photooftheday #beautiful #follow
    #instagram #picoftheday #bhfyp #me #smile #model #likeforlikes #art #beauty #cuteoutfit #cute #ootd
    #likes #look #followforfollowback #fashionblogger #outfit #artsy #aestheticfashion #aesthetic #aestheticoutfit """.format(mainword=mainword, N = N)
    browser = setupsel()
    # Wait so that the pop up doesn't? appear and then load
    browser.implicitly_wait(5)
    browser.get("https://business.facebook.com/creatorstudio?tab=instagram_content_posts&collection_id=all_pages")
    #browser = geturl("https://business.facebook.com/creatorstudio?tab=instagram_content_posts&collection_id=all_pages")
    browser.implicitly_wait(3)
    browser.find_element_by_id('js_3y').click()
    link = browser.find_element_by_link_text("Fil d'actualité Instagram")
    link.get_attribute("href")
    link.click()
    time.sleep(3)

    #description = browser.find_element_by_class_name('_7-2a _5yk1 ads-text-suggestions-focusable')
    #description.send_keys(des_words)
