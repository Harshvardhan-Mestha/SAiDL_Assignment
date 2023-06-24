import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def get_trans(line):
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("http://64.227.154.39:5000/translate")
    driver.implicitly_wait(2)

    hi_input = driver.find_element(by=By.NAME, value="inputSourceText")
    hi_dd = driver.find_element(by=By.NAME, value="inputSourceLanguage")
    en_dd = driver.find_element(by=By.NAME, value="inputTargetLanguage")

    hi_dropdown = Select(hi_dd)
    en_dropdown = Select(en_dd)

    hi_input.send_keys(str(line))
    hi_dropdown.select_by_visible_text("hindi")
    en_dropdown.select_by_visible_text("english")    

    submit_button = driver.find_element(by=By.ID, value="translateButton")
    submit_button.click()
    time.sleep(5)
    #print(driver.page_source)


    trans = driver.find_element(by=By.ID, value="outputTranslatedText")
    align = driver.find_element(by=By.ID, value="outputAlignments")

    #print(trans.get_attribute("value"))
    #print(align.get_attribute("value"))




file1 = open('hi-to-en-input_lang1', 'r')
lines = file1.readlines()
#print(lines[0])

count = 0
i = 0


for line in lines:
    print(i)
    i = i+1
    try:
        get_trans(line)
    except:
        count = count + 1

print("###### --- " + str(count) + " LINES WERE NOT TRANSLATED !!!!!!!!!")
#get_all_trans()
#get_trans("भीषण गर्मी के बीच दिल्ली में बिजली की मांग भी बढ़ गई है")
#get_trans("भडवा गर्दी के पैसों से ख़रीदी है क्या कार")