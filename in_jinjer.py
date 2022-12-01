from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pathlib import Path
import smtplib, ssl

import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.common.alert import Alert

import chromedriver_binary
import os
import os.path
import re
import glob
import pyperclip
import json

import pandas as pd
import jaconv

import shutil
import sys
import base64

from datetime import datetime, date, timedelta
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time

driver.get('https://employee.jinjer.biz/mypage')
time.sleep(5)

iframe = driver.find_element_by_id('jlogin-form-staff')

driver.find_element_by_xpath('/html/body/div[1]/section/section/form/dl[1]/dd/input').send_keys('12399')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/section/form/dl[2]/dd/input').send_keys('000208')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/section/form/dl[3]/dd/input').send_keys('99001016')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/section/form/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/section/main/div[2]/div[2]/ul/li[1]/button').click()
time.sleep(1)

driver.quit()

exit()
