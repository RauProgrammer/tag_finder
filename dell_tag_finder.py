#libraries import
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


#info list
support_list = []

#open tags sheet into dict
with open("caminho da planilha.xlsx com as tags",
          'rb') as tags:
    tags_sheet = pd.read_excel(tags)
tags_dict = tags_sheet.to_dict()

#set driver options
driverOptions = webdriver.ChromeOptions()
driverOptions.add_experimental_option("detach", True)
driverOptions.add_argument("--headless=new")
driverOptions.add_argument("window-size=1366x768")

#set driver configs
driver = webdriver.Chrome(options=driverOptions)

#driver waits and url
driver.implicitly_wait(8)
driver.get("https://www.dell.com/support/home/pt-br")
timeout = 2

#searching in page
assert "Dell" in driver.title

for tag in tags_dict["TAGS"]:
    try:
        # search for TAG
        element_search = driver.find_element(
            "xpath", '//*[@id="mh-search-input"]')
        element_search.clear()
        element_search.send_keys(tags_dict["TAGS"][tag])
        element_search.send_keys(Keys.ENTER)
        time.sleep(timeout)

        try:
            reject_cookies = driver.find_element(
                "xpath", '//*[@id="top"]/div[2]/div[2]/a[1]')
            ActionChains(driver) \
                .click(reject_cookies) \
                .perform()
        except:
            pass

        # click events
        detail_warranty = driver.find_element(
            "xpath", '//*[@id="viewDetailsWarranty"]')
        ActionChains(driver) \
            .click(detail_warranty) \
            .perform()

        # check warranty status
        try:
            #check two different xpaths
            warranty_status = driver.find_element(
                "xpath", '//*[@id="supp-svc-status-txt-2"]/span')
            warranty_status2 = driver.find_element(
                "xpath", '//*[@id="supp-svc-status-txt"]/span')

            if warranty_status.text == "Expirada" or warranty_status2 == "Expirada":
                # get service type text
                contract_info = driver.find_element(
                    "xpath", '//*[@id="termContractsDisplaySelf"]/div/div/div[1]/div[2]/div[1]')
                support_info = contract_info.text
                tags_dict["Serviço"][tag] = support_info
            else:
                pass
        except:
            term_contracts = driver.find_element(
                "xpath", '//*[@id="termContracts"]')
            ActionChains(driver) \
                .click(term_contracts) \
                .perform()
            time.sleep(timeout)

            # get service type text
            contract_info = driver.find_element(
                "xpath", '//*[@id="termContractsDisplaySelf"]/div/div/div[1]/div[2]/div[1]')
            if contract_info == "Keep Your Hard Drive, 5 Year":
                contract_info = driver.find_element(
                    "xpath", '//*[@id="termContractsDisplaySelf"]/div/div/div[1]/div[3]/div[1]')

            support_info = contract_info.text
            tags_dict["Serviço"][tag] = support_info

    except:
        pass

#close window
driver.close()

#print(support_list)
#print(tags_dict)

tag_df = pd.DataFrame(data= tags_dict)

tag_df.to_excel("caminho para gerar a nova planilha.xlsx", index_label=False)