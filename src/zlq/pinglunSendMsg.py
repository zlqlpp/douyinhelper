import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from asyncio.tasks import sleep


sou_suo_guanjianzi="football"
jie_liu_shipinshuliang=3
ping_lun_key1="钱"
ping_lun_key2="能不能"
si_xin_neirong="你好"

driver=''  #### chromeDriver
mouse=''  ####  鼠标操作
 
 #初始化 driver
def initDriver() :
    user_data_dir = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
    user_option = webdriver.ChromeOptions()
    user_option.add_argument(f'--user-data-dir={user_data_dir}')
    driver = webdriver.Chrome(options=user_option)
    print('deiver 初始化完成')
    ## 默认等待时间
    ac = ActionChains(driver)
    driver.implicitly_wait(1)
    
## 打开一个页面
def openPage(url,waitSec):
    ##打开搜索页面
    driver.get(url);
    time.sleep(waitSec)

## 根据class内容查找单个元素
def findElementByClassName(className):
    return driver.find_element(By.CLASS_NAME,className)

## 根据class内容查找元素集合
def findElementSByClassName(className):
    return driver.find_element(By.CLASS_NAME,className)

##在元素上点击鼠标左键，并等待n秒
def leftClick(element,waitSec):
    mouse.move_to_element(element)
    mouse.click(element)
    mouse.perform()
    time.sleep(waitSec)


### 搜索视频后，视频详情页向下点击，并记录视频地址到List中

def getSrc():
    allvideolist=list()
    i=0
    while i<1:
        sleep(2)
        vsrc = driver.find_element(By.CLASS_NAME,'css-1v8b11s-PCopyLinkText').text
        print(vsrc)
        allvideolist.append(vsrc)  ### 收集视频放到list中
        sleep(2)
        sx = driver.find_element(By.CLASS_NAME,'css-1s9jpf8-ButtonBasicButtonContainer-StyledVideoSwitch')
        mouse.move_to_element(sx)
        mouse.click(sx)
        mouse.perform()
        time.sleep(5)
        i+=1
    return allvideolist



def getAllPingLunUsers(videolist):
### 所有的搜出来的 视频的  详细地址，向下滚动评论，把所有评论的作者记录下来
    alluserslist=list()
    vcount = 1
    for e in videolist:
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
                alluserslist.append(pinglun.get_attribute('href'))
            except:
                continue
            
        time.sleep(5)
    return alluserslist

### 给用户发送消息
def sendMsg(userlist):
    if len(userlist)==0:
        print("没有匹配到评论")
    i=1
    usermap = {}
    for dyuser in userlist:
        if dyuser in usermap.keys():
            continue
        usermap[dyuser] = dyuser
        try:
            ###driver.get("https://www.douyin.com/search/"+str(quote(dyuser))+"?type=user");
            driver.get(dyuser);
            time.sleep(6)
            #uurl = driver.find_element(By.CLASS_NAME,'WTCKzPrM').find_elements(By.CLASS_NAME,'B3AsdZT9')[0].get_attribute("href")
            #driver.get(uurl)
            #time.sleep(8)
    
             
    
    
            b = driver.find_element(By.CLASS_NAME,'css-usq6rj-DivMoreActions')  ## 操作的三个小点
             
            #print(b[1].text)
         
            time.sleep(0.5)
            mouse.move_to_element(b).perform() ##鼠标悬停
            mouse.click(b)
            time.sleep(1)
            mouse.perform()
    
            sx = driver.find_element(By.CLASS_NAME,'css-i5wukf-PText')   ##找到发消息
            mouse.move_to_element(sx)
            mouse.click(sx)
            mouse.perform()
            time.sleep(5)
            
     
    
            t = driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block')   ##新页面找到发消息窗
            mouse.move_to_element(t)
            mouse.click(t)
            mouse.perform()
            time.sleep(1)
            print('click over')
            t.send_keys('1')
            time.sleep(3)
            t.send_keys(Keys.ENTER)
            time.sleep(5)
            print("共"+str(len(userlist))+"用户，向第"+str(i)+" 个用户："+str(dyuser)+"----发送消息完成")
            i+=1
        except:
            continue
        
        
        
        
        
##打开搜索页面
openPage("https://www.tiktok.com/search?q="+str(quote(sou_suo_guanjianzi)),8);
#driver.execute_script(r'window.scrollTo(0,500)')
###点击第一个视频，进入视频的播放页面
sx = findElementByClassName('css-1soki6-DivItemContainerForSearch');
leftClick(sx, 1)
time.sleep(8)
print('-------------------')

videolist = getSrc()  ###记录所有视频

userlist = getAllPingLunUsers(videolist);


time.sleep(3)

sendMsg(userlist)
