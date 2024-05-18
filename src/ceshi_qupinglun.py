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





allvideo=list()
allvideo.append('https://www.tiktok.com/@messixronaldo0/video/7363685745380429062?is_from_webapp=1&sender_device=pc&web_id=7362449398222423553')  ### 收集视频放到list中


px=0
durl=""

allusers=list()
count=0


time.sleep(3)
#driver.quit()

### 所有的搜出来的 视频的  详细地址
vcount = 1
for e in allvideo:
    print(e)
    driver.get(e) ##打开地址
    print("共 "+str(jie_liu_shipinshuliang)+" 个视频，现在处理第："+str(vcount))
    vcount += 1
    time.sleep(4)

    for i in range(1,10):##向下滚动
        driver.execute_script('window.scrollTo(0,'+str(i*500)+')')
        time.sleep(0.2) 


    pl = driver.find_elements(By.CLASS_NAME,'css-1i7ohvi-DivCommentItemContainer')  ##所有的 评论

    time.sleep(1)
    if pl=="":
        continue
    for e in pl:  ## 打印所有评论
        try:
            pinglun = e.find_element(By.CLASS_NAME,'css-fx1avz-StyledLink-StyledUserLinkName') ###评论者
            print(pinglun.get_attribute('href'))
            print('------------------------------------------')
            ##allusers.append(pinglun)
        except:
            continue
        
    time.sleep(5)
if len(allusers)==0:
    print("没有匹配到评论")
i=1
usermap = {}
for dyuser in allusers:
    if dyuser in usermap.keys():
        continue
    usermap[dyuser] = dyuser
    try:
        ###driver.get("https://www.douyin.com/search/"+str(quote(dyuser))+"?type=user");
        driver.get(dyuser);
        time.sleep(10)
        #uurl = driver.find_element(By.CLASS_NAME,'WTCKzPrM').find_elements(By.CLASS_NAME,'B3AsdZT9')[0].get_attribute("href")
        #driver.get(uurl)
        #time.sleep(8)

         

        pl = driver.find_element(By.CLASS_NAME,'hLIm2dFu')  ##ty_H89Vr 长江专用
        time.sleep(3)
        b = pl.find_elements(By.TAG_NAME,'button')
         
        #print(b[1].text)
     
        time.sleep(0.5)
        ac.move_to_element(b[1]).perform()
        time.sleep(1)
        ac.click(b[1])
        ac.perform()

         
        time.sleep(3)

        t = driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-ltr')  
        t.send_keys(si_xin_neirong)
        time.sleep(3)
        t.send_keys(Keys.ENTER)
        time.sleep(5)
        print("共"+str(len(allusers))+"用户，向第"+str(i)+" 个用户："+str(dyuser)+"----发送消息完成")
        i+=1
    except:
        continue