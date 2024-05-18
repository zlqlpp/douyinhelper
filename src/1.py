import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

user_data_dir = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()

user_option.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=user_option)
 


sou_suo_guanjianzi="football"
jie_liu_shipinshuliang=3
ping_lun_key1="钱"
ping_lun_key2="能不能"
si_xin_neirong="你好"




##搜索视频
driver.get("https://www.tiktok.com/search?q="+str(quote(sou_suo_guanjianzi)));

time.sleep(8)



ac = ActionChains(driver)

driver.implicitly_wait(1)
#driver.execute_script(r'window.scrollTo(0,500)')

###进到视频详情页面
sx = driver.find_element(By.CLASS_NAME,'css-1soki6-DivItemContainerForSearch')
ac.move_to_element(sx)
ac.click(sx)
ac.perform()
time.sleep(1)
 
###----------------------------------------
time.sleep(5)
sx = driver.find_elements(By.CLASS_NAME,'css-1i7ohvi-DivCommentItemContainer')
 
print(sx[0])
ac.move_to_element(sx[0])
ac.context_click(sx[0])
ac.perform()
time.sleep(2)
print('click over')
time.sleep(2)
driver.execute_script(r'window.scrollTo(0,700)')
time.sleep(2)
driver.execute_script(r'window.scrollTo(0,800)')
px=0
durl=""
allvideo=list()
allusers=list()
count=0
while count<jie_liu_shipinshuliang:
    
    ## 找到视频，视频div大标记
    pl = driver.find_elements(By.CLASS_NAME,'search-result-card')
    #print('找到主标记')
    time.sleep(0.5)
    #print(len(pl))
    #print(pl[ind])
    
    
 

    ## 在视频上点 右键
    try:
        for e in pl:
            try:
                #divflag = e.find_element(By.TAG_NAME,'div').get_attribute('class')
                divflag = e.find_element(By.CLASS_NAME,'Ys1zFCEZ')##视频div大标记--》视频二标记
                #print(divflag)
                #if divflag=='':
                #    continue
                actived =divflag.find_element(By.ID,"sliderVideo").get_attribute("data-e2e")
                #print(actived)
                if actived == "feed-active-video":##视频div大标记--》视频二标记--》视频div
                    #print('找到正播放的视频')
                    ac.move_to_element(e)
                    ac.context_click(e)
                    ac.perform()

                    time.sleep(0.1)
                    hh = e.find_element(By.CLASS_NAME,'RryDljCo') 
                    if durl!=hh.get_attribute("href") and 'douyin' in hh.get_attribute("href"):
                        ##print(hh.get_attribute("href"))
                        allvideo.append(hh.get_attribute("href"))
                        print("共"+str(jie_liu_shipinshuliang)+"个视频，当前找到"+str(count)+" 个：" )
                        count+=1
                        durl=hh.get_attribute("href")
                        
                        break
            except:
                continue
             
            
                  
           ### 找到 详情页的链接 
            
        px+=100
        t = 'window.scrollTo(0,'+str(px)+')'
        driver.execute_script(t)
        time.sleep(0.1)
        continue
    finally:
        px+=100
        t = 'window.scrollTo(0,'+str(px)+')'
        driver.execute_script(t)
        time.sleep(0.5)
        continue
 



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


    pl = driver.find_elements(By.CLASS_NAME,'xzjbH9pV')

    time.sleep(1)
    if pl=="":
        continue
    for e in pl:  ## 打印所有评论
        try:
            pinglun = e.find_element(By.CLASS_NAME,'sU2yAQQU').text
            if pinglun!="" and (ping_lun_key1 in pinglun or ping_lun_key1 in pinglun   ): 
                print(e.find_element(By.CLASS_NAME,'b2riW_HJ').text) ##抖音号
                print(e.find_element(By.CLASS_NAME,'sU2yAQQU').text) ## 评论的内容
                print('------------------------------------------')
                allusers.append(e.find_element(By.CLASS_NAME,'hY8lWHgA').get_attribute("href"))
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