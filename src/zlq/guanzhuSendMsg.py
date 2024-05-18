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


def getuseraddrbysearchid():
    openPage('https://www.tiktok.com/search?q=footballvoicess',5); ##先点到 帐号 页
    zhanghaotag = findElementByClassName('css-4cma0b-DivTab');
    leftClick(zhanghaotag,3)
    
    css-18z0n14-StyledLink-StyledDivInfoWrapper  ##取
    print();
    
    return 

initDriver();

## 通过用id搜索找到 用户的地址
useraddr=getuseraddrbysearchid();

##打开用户主页面，捞取用户的所有粉丝
fansList = getfansListByUserAddr(useraddr);

viewFansVideoAndDianZanGuanzhu(fansList);

monitorTiXingList();