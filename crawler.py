from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from retry import retry

link_preco = 'https://tableaupub.ccee.org.br/t/CCEE/views/PreoHistrico/HistricodoPreoHorrio?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Ftableaupub.ccee.org.br%2F&%3Aembed_code_version=3&%3Atabs=no&%3Atoolbar=yes&%3Aiid=4&%3AisGuestRedirectFromVizportal=y&%3Adisplay_count=no&%3Aorigin=viz_share_link&%3AshowShareOptions=false&%3Aalerts=no&%3Arefresh=yes&%3Adisplay_spinner=no&%3AloadOrderID=1'
link_gsf = 'https://tableaupub.ccee.org.br/t/CCEE/views/PainelGerao/MRE?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Ftableaupub.ccee.org.br%2F&%3Aembed_code_version=3&%3Atabs=yes&%3Atoolbar=yes&%3AshowAppBanner=false&%3Adisplay_spinner=no&iframeSizedToWindow=true&%3AloadOrderID=0'
driver = webdriver.Chrome()

@retry(tries = 5,delay = 1)
def find_and_click(selector,text,index = 0):
    driver.find_elements(selector,text)[index].click()

@retry(tries = 5,delay = 1)
def find_and_print(selector,text):
    elements = driver.find_elements(selector,text)
    if elements == []:
        raise ValueError
    for element in elements:
        print(element.get_attribute('class'))

driver.get(link_preco)

find_and_click(By.CSS_SELECTOR,'div.tabStoryPointContent.tab-widget',2)
find_and_click(By.CSS_SELECTOR,'div#download-ToolbarButton.tabToolbarButton.tab-widget.download')
find_and_click(By.CSS_SELECTOR,"button[class = 'f1odzkbq low-density']",2)
find_and_click(By.CSS_SELECTOR,"div[class = 'hidden-icon-wrapper_f72siau']",1)
sleep(1)
find_and_click(By.CSS_SELECTOR,"button[class = 'fycmrtt low-density']")
sleep(1)

driver.get(link_gsf)

find_and_click(By.CSS_SELECTOR,"div[class = 'tabToolbarButton tab-widget download']")
find_and_click(By.CSS_SELECTOR,"button[class = 'f1odzkbq low-density']",2)
find_and_click(By.CSS_SELECTOR,"div[class = 'hidden-icon-wrapper_f72siau']",7)
sleep(1)
find_and_click(By.CSS_SELECTOR,"button[class = 'fycmrtt low-density']")
sleep(5)
