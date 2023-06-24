import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("http://64.227.154.39:5000")
driver.implicitly_wait(2.5)


hi = driver.find_element(by=By.NAME, value="inputSourceLang")
en = driver.find_element(by=By.NAME, value="inputTargetLang")

hi_input = driver.find_element(by=By.NAME, value="inputSourceSentence")
en_input = driver.find_element(by=By.NAME, value="inputTargetSentence")

alignments = driver.find_element(by=By.NAME, value="inputAlignments")

#for line in lines:

hi.send_keys("Hindi")
en.send_keys("English")
hi_input.send_keys("यदि आप तुरंत डॉक्टर से संपर्क करे")
en_input.send_keys("Contact the doctor immediately if you")
alignments.send_keys("0-4 1-5 2-3 3-2 5-0 6-0 6-1")

submit_button = driver.find_element(by=By.ID, value="gcmGenButton")

submit_button.click()
time.sleep(10)
sens = driver.find_elements(By.TAG_NAME, 'td')

for i in sens:
    print(i.text)
# cms = table.find_elements(By.TAG_NAME, 'tr')

# for e in cms:
#     #sen = e.find_element(By.CLASS_NAME, 'row-index text-center')
#     print(e.text)