import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from asyncio.tasks import sleep

user_data_dir = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()

user_option.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=user_option)
 


sou_suo_guanjianzi="football"
jie_liu_shipinshuliang=3
ping_lun_key1="钱"
ping_lun_key2="能不能"
si_xin_neirong="你好"




##打开搜索页面
#driver.get("https://www.tiktok.com/search?q="+str(quote(sou_suo_guanjianzi)));

#time.sleep(8)


## 默认等待时间
ac = ActionChains(driver)
driver.implicitly_wait(1)
#driver.execute_script(r'window.scrollTo(0,500)')

###点击第一个视频，进入视频的播放页面




driver.get('https://www.tiktok.com/@cr7_7m7m');
time.sleep(3)

b = driver.find_element(By.CLASS_NAME,'css-usq6rj-DivMoreActions')  ## 操作的三个小点
         
        #print(b[1].text)
     
time.sleep(0.5)
ac.move_to_element(b).perform() ##鼠标悬停
ac.click(b)
time.sleep(1)
ac.perform()

sx = driver.find_element(By.CLASS_NAME,'css-i5wukf-PText')   ##找到发消息
ac.move_to_element(sx)
ac.click(sx)
ac.perform()
time.sleep(5)
        
 

t = driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block')   ##新页面找到发消息窗
ac.move_to_element(t)
ac.click(t)
ac.perform()
time.sleep(1)
print('click over')
t.send_keys('1')
time.sleep(3)
t.send_keys(Keys.ENTER)
time.sleep(5)
 