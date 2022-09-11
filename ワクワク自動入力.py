""" タレパレ自動入力 使用方法
① python, importの環境構築 (詳しくは俺まで)
② 22,23行目にログインメールアドレス，パスワードを記入
③ 33行目の入力したい開始日を入力(デフォルトは，1日から開始)
"""

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import datetime
import random
 
# Chromeを指定して起動
driver = webdriver.Chrome()
driver.get('https://pepup.life/users/sign_in')
# 起動待ち
time.sleep(1)

# ログイン
email = ""
password = ""

mailbox = driver.find_elements(By.XPATH, "//*[@id='sender-email']")
passbox = driver.find_elements(By.XPATH, "//*[@id='user-pass']")
mailbox[0].send_keys(email)
passbox[0].send_keys(password)
mailbox[0].submit()

# 日付設定
now_month = datetime.datetime.now().strftime('%Y/%-m')
start_date = 1
end_date = (int)(datetime.datetime.now().strftime('%-d'))

# 記入内容のまとめ
strs = [
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[3]/div[2]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[4]/div[2]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[5]/div[2]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[5]/div[3]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[5]/div[4]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[5]/div[5]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[5]/div[6]/label/input",
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[6]/div[2]/label/input", # 8月だけ
  "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[2]/button"
]

# 記入実行
for i in range(start_date, end_date+1):
  # 遷移URLの算出
  url = 'https://pepup.life/scsk_mileage_campaigns/' + str(now_month) + "/" + str(i)
  driver.get(url)

  # 歩数入力
  e = driver.find_elements(By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[1]/input")[0]
  if (not e.get_attribute("value")):
    #e.clear()
    e.send_keys(str(random.randint(9000, 15000)))
    
  # 睡眠時間入力
  e = driver.find_elements(By.XPATH, "//*[@id='app']/div/div[2]/div/div[2]/div[3]/form/div[1]/div[2]/input")[0]
  if (not e.get_attribute("value")):
    #e.clear()
    e.send_keys(str(random.randint(60, 85)/10))
    
  for st in strs:
    e = driver.find_elements(By.XPATH,st)[0]
    if (not e.is_selected()):
      e.click()
    
# ブラウザを閉じる
driver.close()

