from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = input("chrome driver binary location:")
# C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe
browser = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
browser.maximize_window()

ncov_reports_url = "https://3g.dxy.cn/newh5/view/pneumonia?scene=1&clicktime=1579593820&enterid=1579593820&from=timeline&isappinstalled=0"

while True:
    browser.get(ncov_reports_url)
    time.sleep(0.618)
    src = browser.page_source
    if re.search('福建', src) is None:
        print('Fujian was clean at', time.asctime(time.localtime()))
        time.sleep(66.666)
    else:
        break

print('******Warning!******')
