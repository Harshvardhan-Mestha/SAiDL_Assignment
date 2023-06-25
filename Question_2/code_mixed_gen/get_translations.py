import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException



def get_trans(line):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--disable-notifications')

    driver = webdriver.Chrome(options=options)
    driver.get("http://64.227.154.39:5000/translate")
    driver.implicitly_wait(3)

    hi_input = driver.find_element(by=By.NAME, value="inputSourceText")
    hi_dd = driver.find_element(by=By.NAME, value="inputSourceLanguage")
    en_dd = driver.find_element(by=By.NAME, value="inputTargetLanguage")
    
    hi_dropdown = Select(hi_dd)
    en_dropdown = Select(en_dd)

    hi_input.send_keys(str(line))
    hi_dropdown.select_by_value("hi")
    en_dropdown.select_by_value("en")    

    submit_button = driver.find_element(by=By.ID, value="translateButton")
    
    submit_button.click()

    time.sleep(2)
    
    #print(driver.page_source)




    try:
        try:
            WebDriverWait(driver, 1).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass
        
        trans = driver.find_element(by=By.ID, value="outputTranslatedText")
        align = driver.find_element(by=By.ID, value="outputAlignments")

        #print(trans.get_attribute("value"))
        #print(align.get_attribute("value"))
        return [trans.get_attribute("value"),align.get_attribute("value")]

    except UnexpectedAlertPresentException:
         WebDriverWait(driver, 1).until(EC.alert_is_present())
         driver.switch_to.alert.accept()
         return["",""]

    #     f_trans.write(str(trans.get_attribute("value")))
    #     f_trans.write('\n')
    #     f_align.write(str(align.get_attribute("value")))
    #     f_align.write('\n')

    #     f_trans.close()
    #     f_align.close()
    # except:
    #     f_trans.write('^')
    #     f_trans.write('\n')
    #     f_align.write('^')
    #     f_align.write('\n')
        
        
def save_trans(arr):
        f_trans = open('/Users/harshvardhanmestha/Desktop/code_mixed_gen copy/hi-to-en-input_lang2', 'a')
        f_align = open('/Users/harshvardhanmestha/Desktop/code_mixed_gen copy/hi-to-en-input_parallel_alignments', 'a')
        if(len(arr[0])==0):
            f_trans.write('^')
            f_trans.write('\n')
            f_align.write('^')
            f_align.write('\n') 
        else:
            f_trans.write(arr[0])
            f_trans.write('\n')
            f_align.write(arr[1])
            f_align.write('\n')
    
   



file1 = open('hi-to-en-input_lang1', 'r')
lines = file1.readlines()
#print(lines[0])

i = 0




for i in range(27,len(lines)):
    #print(lines[i])
    final = get_trans(str(lines[i]))
    save = save_trans(final)
    print("LINE  "+str(i+1)+"  processed :"+lines[i][0:15])
    
    

    

        


    

#print("###### --- " + str(count) + " LINES WERE NOT TRANSLATED !!!!!!!!!")
# #get_all_trans()
# get_trans("भीषण गर्मी के बीच दिल्ली में बिजली की मांग भी बढ़ गई है")
# get_trans("भडवा गर्दी के पैसों से ख़रीदी है क्या कार")
# get_trans("सुन्दर आंटी रंडी से लुंड चुसवाया")