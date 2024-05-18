import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from asyncio.tasks import sleep
from selenium.common.exceptions import NoSuchElementException

user_data_dir = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()

user_option.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=user_option)
 


sou_suo_guanjianzi="football"
jie_liu_shipinshuliang=3
ping_lun_key1="钱"
ping_lun_key2="能不能"
si_xin_neirong="你好"


def dianzan():
    #双击点赞
    fsvideo1 = driver.find_element(By.CLASS_NAME,'css-1tunefa-DivVideoContainer')
    ac.move_to_element(fsvideo1)
    ac.click(fsvideo1)
    ac.click(fsvideo1)
    ac.perform()
    print('---------双击点赞---------')
    time.sleep(1)
    time.sleep(5)
    


def playNextVideo():
     #播放下一个视频
    # try:
    nextvideo = driver.find_element(By.CLASS_NAME,'css-1s9jpf8-ButtonBasicButtonContainer-StyledVideoSwitch')
    if not nextvideo.is_displayed():
        # print("----元素被隐藏-----")
        print("-----无下一条视频-----")
        return 0
    ac.move_to_element(nextvideo)
    ac.click(nextvideo)
    ac.perform()
    print('---------播放下一个视频---------')
    time.sleep(1)
    #浏览5秒
    time.sleep(5)
    return 1
    
    
#关注账号
def guanzhu():
    gzzh = driver.find_element(By.CLASS_NAME,'css-1pcikqk-Button')
    ac.move_to_element(gzzh)
    ac.click(gzzh)
    ac.perform()
    print("--------关注账号----------")
    time.sleep(1)
    time.sleep(8)


##打开搜索页面
driver.get("https://www.tiktok.com/search?q="+str(quote(sou_suo_guanjianzi)));

time.sleep(8)


## 默认等待时间
ac = ActionChains(driver)
driver.implicitly_wait(1)

#点击账号
zh = driver.find_element(By.CLASS_NAME,'css-4cma0b-DivTab')
ac.move_to_element(zh)
ac.click(zh)
ac.perform()
print('---------点击账号查询账号列表----------')
time.sleep(1)
time.sleep(8)

# #点击第一个账号
firstOne = driver.find_element(By.CLASS_NAME,'css-1d5vh4i-DivLink')
ac.move_to_element(firstOne)
ac.click(firstOne)
ac.perform()
print('---------点击第一个账号---------')
time.sleep(1)
time.sleep(8)

#点击查看粉丝
gz = driver.find_elements(By.CLASS_NAME, 'css-1ubs7lq-SpanUnit')[1]
ac.move_to_element(gz)
ac.click(gz)
ac.perform()
print('---------点击查看粉丝---------')
time.sleep(1)
time.sleep(8)


fslist = driver.find_elements(By.CLASS_NAME, 'css-5c23qb-StyledLink-StyledUserInfoLink')

# 想要获取的元素数量
fixed_number = 30
 
# 实际获取的元素数量
actual_number = 0
 
# 结果列表
fixed_elements = []

#点赞视频数
playVideo_num = 3

# 循环遍历元素直到获取固定数量
for element in fslist:
    fixed_elements.append(element.get_attribute('href'))
    actual_number += 1
    if actual_number >= fixed_number: 
        break

print("------element------")
print(fixed_elements)


for li in fixed_elements:
    driver.get(li);
    print('当前浏览---'+li)

    
    # #浏览粉丝主页第一个视频 
    try :
        fsvideo = driver.find_element(By.CLASS_NAME,'css-x6f6za-DivContainer-StyledDivContainerV2')
        ac.move_to_element(fsvideo)
        ac.click(fsvideo)
        ac.perform()
        print('---------浏览粉丝第1个视频---------')
        time.sleep(1)
        #浏览5秒
        time.sleep(5)
           
        #双击点赞
        dianzan()
        
        i = 1
        
        while i<playVideo_num:
            result = playNextVideo()
            if result == 0 :
                print('-----视频不足'+str(playVideo_num)+'条-----')
                break
            else:
                j = i+1
                print('---------浏览粉丝第'+str(j)+'个视频---------')
                dianzan()
                if i == playVideo_num-1:
                    guanzhu()
                    break
                else:
                    i+=1
            
            
    except NoSuchElementException:
         print('---------无视频---------')
         time.sleep(8)
         continue

