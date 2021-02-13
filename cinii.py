#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver 
import time 
import urllib.request as req
import csv
import datetime
from selenium.webdriver.chrome.options import Options


# In[ ]:


val = input("Keyword:")
options = Options()
options.add_argument("--headless")
url = 'https://ci.nii.ac.jp/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)


# In[ ]:


search = driver.find_element_by_name('q')   # HTML内で検索ボックス(name='q')を指定する
keyword = val
search.send_keys(keyword)


# In[ ]:


search_button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form[1]/div/div/div/div[1]/div[2]/div[2]/button') # 検索を実行
search_button.click()
time.sleep(5)


# In[ ]:


csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "Desktop/cinii" + csv_date + val + ".csv"
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
 
writer = csv.writer(f, lineterminator="\n") 
csv_header = ["タイトル","著者","URL"]
writer.writerow(csv_header)


# In[ ]:


count = len(driver.find_elements_by_class_name('pagingbtn'))

print(count)


# In[ ]:


i = 0
while True:
    i = i + 1
    time.sleep(3)
    
    for elem in driver.find_elements_by_class_name('taggedlink'):  
        author = elem.find_element_by_xpath('../../dd/p[@class="item_subData item_authordata"]')
        csvlist = []
        csvlist.append(elem.text)
        csvlist.append(author.text)
        csvlist.append(elem.get_attribute('href'))
        writer.writerow(csvlist)

    next_link = driver.find_element_by_css_selector("a.paging_next")
    driver.get(next_link.get_attribute('href'))
    if i > 3 :
        break


# In[ ]:


driver.quit()

