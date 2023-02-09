
import selenium
import html
import pyperclip as pc
import json

import pyautogui
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import  Service
from selenium.webdriver.common.action_chains import ActionChains



import execute
import time
from selenium.webdriver.common.keys import Keys

def to_be_used(num):
    bool = (driver.execute_script("""function myFunction(p1) {
    var test =document.getElementsByClassName("l5k26z4s snfsxcfg oysqpf8i qwtvmjv2 kiex77na lgsfgr3h mcogi7i5 ih1xi9zn ippphs35 a53abz89")[p1].innerText;
    if(test != 'See ad details')
    {
    test = 0;
    }
    return Boolean(test) 
    }; return myFunction("""+str(num)+""")"""))
    return bool
def peki(post_num):
    try:
        time.sleep(1)
        js_go_back = """var xPathRes = document.evaluate ('//*[@id="facebook"]/body/div[""" + str(post_num + 4) + """]/div[2]/div/div/div/div/div[1]/div/div/div/span/div/div[2]/div/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);setTimeout(xPathRes.singleNodeValue.click(),2000);"""
        print(js_go_back)
        print(post_num+4)
        driver.execute_script(js_go_back)
    except:
        peki(post_num)
def get_the_dates():
    print("+ amin kim ? - amin feryadi efendim")
    test = (driver.find_element(By.XPATH, ("/html/body")))
    tobereturned = ""
    for x in test.text.split("\n"):
        if(x != ""):
            pass
        if(x[:18] == "Started running on"):
            tobereturned = x
    print(")))))))))))))))))))",tobereturned)
    return tobereturned
def read_page():
    test = (driver.find_element(By.XPATH, ("/html/body")))

    is_more_info = False
    hastags = ""
    internals = ""
    internals2 = ""
    link = "https://www.facebook.com/ads/library/?id="
    moreinf_counter = 0
    id = ""
    print("hey  :3    !")
    for x in test.text.split("\n"):
        if(moreinf_counter == 20):
            if(x != "About ads and data use") and(x != "Open Drop-dow") :
                internals += x
        if(x == "Open Drop-down"):
            moreinf_counter+=1
        if(x != ""):
            pass
        if(x[:3] == "ID:"):
            id = x[4:]
    link += id
    search= False

    for x in test.text.split("\n"):
        if(search == True) and (x != "Open Drop-down" ) and (x != "About ads and data use"):
            internals2 +=x

        if(x == ("ID: "+id)):
            search = True

    return id,link,internals2

conver_me_to_json_pls =[]
s = Service('C:/Users/cdres/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#driver.maximize_window()
to_be_searched = "akbank"
driver.implicitly_wait(0.5)
driver.get("https://www.facebook.com/ads/library/")



action = webdriver.ActionChains(driver)

# to scroll till page bottom
time.sleep(1)
driver.execute_script("""document.querySelectorAll('[data-visualcompletion="ignore"]')[1].querySelectorAll('input')[0].click()""")
time.sleep(1)

xpath = """//input[@placeholder="Search by keyword or advertiser"]"""
name = "Search by keyword or advertiser"
clasy = "rnv9nx9r fqe99cye rws5ya1x l5fv8vmd do23leof a6u30k36 mue9ndml h1h4usya bvxmbkr6 dgpf1xc5 e946d6ch jjq1mtj1 q2nlfsy2 s916jpeb gue7836a ceubdte7 mnqrf277 pesago7c b6ewvobd ih2s8k95 mqteepqw berxdx8z egkesoaz qi2u98y8 ikxir1m9 iajz466s iihkvusu jlgdmla5"
print("input[XPATH="+ xpath  +"]")
username = driver.find_element(By.XPATH, xpath)
#//*[@id="js_zd"]/div/div[1]
#username2.clear()
#username2.send_keys(to_be_searched1)

username.clear()
username.send_keys(to_be_searched)
username.send_keys(Keys.ENTER)
links = []
print(username)
time.sleep(3)


path0 ="""('//*[@id="content"]/div/div/div/div[6]/div[1]/div/div/div[2]/div[3]/div[1]/div["""
path2 = "]/div/div[2]/div/span/div/div/div');"

attempt = 1


js_command_set_path = """var xPathRes = document.evaluate ("/html/body/div[1]/div[1]/div[1]/div/div/div/div[6]/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/div/div[2]/div/span/div/div/div", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);"""
js_command_execute_path = "xPathRes.singleNodeValue.click()"
give_up = True
js = """document.getElementsByClassName('l5k26z4s snfsxcfg oysqpf8i qwtvmjv2 kiex77na lgsfgr3h mcogi7i5 ih1xi9zn ippphs35 a53abz89')["""
js2 = """].click()"""
#driver.execute_script(js+str(1)+js2)


get_the_link_js= """var xPathRes = document.evaluate ('//div[@class ="l5k26z4s svdiirva jbfqbifr all6rvt3 kxmygt8f svz86pwt q3s3exew d8d6zf0d p66o6c86 a53abz89"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); xPathRes.singleNodeValue.click();"""
#var xPathRes = document.evaluate ('//div[@class ="l5k26z4s svdiirva jbfqbifr all6rvt3 kxmygt8f svz86pwt q3s3exew d8d6zf0d p66o6c86 a53abz89"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); xPathRes.singleNodeValue.click();
post_num= 1
page_num= 2
open_link_js ="""document.querySelectorAll('[class="_3qn7 _61-0 _2fyi _3qng"]')["""+str(31 + post_num)+"""].querySelector('[class="jwy3ehce"]').click()"""




link = ""
id = ""
internals = ""
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
try:
    while give_up == True :
        #try:

            #print(pass_to_be)

            while(to_be_used(page_num) == False):
                    page_num +=1

            pass_to_be = to_be_used(page_num)


            print("post")
            ls_of_info= {}

            time.sleep(3)

            bk = driver.find_elements(By.XPATH, '//img[@class="_8nqq img"]')[post_num]
            isim = (bk.get_attribute('alt'))
            resim = html.unescape(bk.get_attribute('src'))

            #print('[T]', resim)
            #print('[TT]', isim)
            #print('[TT999]', post_num+4)
            ls_of_info["name"] = isim
            ls_of_info["profile_pic"] = resim
            ls_of_info["order"] = post_num



            driver.execute_script(js + str(page_num) + js2)
            time.sleep(1)
            id,link,internals =read_page()
            time.sleep(1)

            ls_of_info["id"] = id
            ls_of_info["link"] = link
            ls_of_info["internals"] = internals

            peki(post_num)

            time.sleep(1)
            print("sowy :3")



            page_num += 1
            post_num += 1
            print(ls_of_info)
            conver_me_to_json_pls.append(ls_of_info)
except Exception as e :
    print("!!!!!!!!!!!!!!!!!!ERORORORORORORORORRO!!!!!!!!!!!!!!!!!!!1")
    print(e)

print(conver_me_to_json_pls)
print("son")
print(post_num)
dte = ""
for x in conver_me_to_json_pls :
    driver.get(x["link"])
    time.sleep(3)
    dte = get_the_dates()
    print(dte)
    x["hurma"] = dte
newpath = r'C:\Users\cdres\PycharmProjects\fb3den\data'
if not os.path.exists(newpath):
    os.makedirs(newpath)

print("json")
with open("data/dtest.json", "w") as outfile:
    json.dump(conver_me_to_json_pls, outfile)
