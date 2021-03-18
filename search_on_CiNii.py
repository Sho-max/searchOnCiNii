from selenium import webdriver 
import time 
import urllib.request as req
import csv
import datetime
import chromedriver_binary
import sys

    
#     キーワードの定義
val = input("Keyword:")
url = 'https://ci.nii.ac.jp/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

#     Chrome driverを起動
search = driver.find_element_by_name('q')
# HTML内で検索ボックス(name='q')を指定する
keyword = val
search.send_keys(keyword)

#     CiNii上で検索
search_button = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form[1]/div/div/div/div[1]/div[2]/div[2]/button') # 検索を実行
search_button.click()
time.sleep(5)

#     CSVデータをデスクトップに作成
csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "Desktop/cinii" + csv_date + keyword + ".csv"
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")
#　　　CSVに書き込む内容を定義
writer = csv.writer(f, lineterminator="\n")
csv_header = ["タイトル","著者","URL"]
writer.writerow(csv_header)

#     ページ遷移
while True:

    for elem in driver.find_elements_by_class_name('taggedlink'):
        author = elem.find_element_by_xpath('../../dd/p[@class="item_subData item_authordata"]')
        csvlist = []
        csvlist.append(elem.text)
        csvlist.append(author.text)
        csvlist.append(elem.get_attribute('href'))
        writer.writerow(csvlist)

    try:
        time.sleep(5)
        driver.find_element_by_class_name('paging_next.btn.pagingbtn').click()
    except:
        driver.close()
        driver.quit()
        sys.stdout.write("完了しました")
        break
