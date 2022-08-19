from selenium import webdriver
from Screenshot import Screenshot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome(ChromeDriverManager().install()) #options=options
ob = Screenshot.Screenshot()

driver.get("https://www.zeny.cz/zaujalo-nas/blogerka-ema-rande-v-brdech-999.html")

#clicks on cmp pop up
driver.find_element(By.ID, "didomi-notice-agree-button").click()

#clicks through 250 times on "další články" and takes a screenshot
for i in range(0, 250):
    time.sleep(1)


    driver.find_element(By.CLASS_NAME, "flexible-articles__secondary-title--wrapper").click()
    element = driver.find_element(By.CLASS_NAME,"article-body")
    img_url = ob.get_element(driver, element, r'.') #, image_name=str(savename))
    print(driver.current_url.rsplit('/', 1)[1])
    savename = driver.current_url.rsplit('/', 1)[1] + '.png'
    os.rename('clipping_shot.png', str(savename))