import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from asyncio.tasks import sleep
from selenium.common.exceptions import NoSuchElementException
from _ast import If

user_data_dir = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'

user_option = webdriver.ChromeOptions()

user_option.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=user_option)
 


sou_suo_guanjianzi="football"
jie_liu_shipinshuliang=3
ping_lun_key1="钱"
ping_lun_key2="能不能"
si_xin_neirong="你好"


#是否有未读消息
def unread():
    try:
        driver.find_element(By.CLASS_NAME,'css-16bbtsh-SupBadge')
        return 1
    except NoSuchElementException:
        print("---无未读消息---")
        return 0
    

##打开搜索页面
driver.get("https://www.tiktok.com");

time.sleep(8)

## 默认等待时间
ac = ActionChains(driver)
driver.implicitly_wait(1)
#driver.execute_script(r'window.scrollTo(0,500)')

#是否有未读消息
b = unread()

if b == 1 : 
    #查看通知
    tz = driver.find_element(By.CLASS_NAME,'css-1g0p6jv-StyledInboxIcon')
    ac.move_to_element(tz)
    ac.click(tz)
    ac.perform()
    time.sleep(1)
    
    time.sleep(8)
    print('---------查看通知---------')
    
    #查看粉丝
    fs = driver.find_element(By.CLASS_NAME,'css-7gu37x-ButtonGroupItem')
    ac.move_to_element(fs)
    ac.click(fs)
    ac.perform()
    time.sleep(1)
    
    time.sleep(8)
    print('---------查看粉丝---------')






#
# #点击查看粉丝
# gz = driver.find_elements(By.CLASS_NAME, 'css-1ubs7lq-SpanUnit')[1]
# ac.move_to_element(gz)
# ac.click(gz)
# ac.perform()
# time.sleep(1)
#
# time.sleep(8)
#
#
# print('---------点击查看粉丝---------')
#
# #点击进入粉丝页面
# fs1 = driver.find_element(By.CLASS_NAME,'css-k0d282-SpanNickname')
# ac.move_to_element(fs1)
# ac.click(fs1)
# ac.perform()
# time.sleep(1)
#
# time.sleep(8)
#
# print('---------点击进入粉丝主页---------')
#
# def dianzan():
#     #双击点赞
#     fsvideo1 = driver.find_element(By.CLASS_NAME,'css-1k866u7-DivPhotoWrapper')
#     ac.move_to_element(fsvideo1)
#     ac.click(fsvideo1)
#     ac.click(fsvideo1)
#     ac.perform()
#     time.sleep(1)
#
#     time.sleep(20)
#     print('---------双击点赞---------')
#
# # #浏览粉丝主页第一个视频 
# try :
#     fsvideo = driver.find_element(By.CLASS_NAME,'css-x6f6za-DivContainer-StyledDivContainerV2')
#     ac.move_to_element(fsvideo)
#     ac.click(fsvideo)
#     ac.perform()
#     time.sleep(1)
#     #浏览5秒
#     time.sleep(5)
#     print('---------浏览粉丝视频---------')
#
#
#     #双击点赞
#     dianzan()
#
#     #播放下一个视频
#     nextvideo = driver.find_element(By.CLASS_NAME,'css-1s9jpf8-ButtonBasicButtonContainer-StyledVideoSwitch')
#     ac.move_to_element(nextvideo)
#     ac.click(nextvideo)
#     ac.perform()
#     time.sleep(1)
#     #浏览5秒
#     time.sleep(5)
# #
# #     print('---------双击点赞---------')
# except NoSuchElementException:
#      print('---------无视频---------')
#      driver.back()
#      time.sleep(20)
#
#
#































# ###点击第一个视频，进入视频的播放页面
# sx = driver.find_element(By.CLASS_NAME,'css-1soki6-DivItemContainerForSearch')
# ac.move_to_element(sx)
# ac.click(sx)
# ac.perform()
# time.sleep(1)
# ac.click(sx)
# ac.perform()
#
# time.sleep(8)
# print('-------------------')
#
#
# allvideo=list()
# def getSrc():
#
#     i=0
#     while i<1:
#         sleep(2)
#         vsrc = driver.find_element(By.CLASS_NAME,'css-1v8b11s-PCopyLinkText').text
#         print(vsrc)
#         allvideo.append(vsrc)  ### 收集视频放到list中
#         sleep(2)
#         sx = driver.find_element(By.CLASS_NAME,'css-1s9jpf8-ButtonBasicButtonContainer-StyledVideoSwitch')
#         ac.move_to_element(sx)
#         ac.click(sx)
#         ac.perform()
#         time.sleep(5)
#         i+=1
#     return 
#
# getSrc()
#
#
# px=0
# durl=""
#
# allusers=list()
# count=0
#
#
# time.sleep(3)
# #driver.quit()
#
# ### 所有的搜出来的 视频的  详细地址
# vcount = 1
# for e in allvideo:
#     print(e)
#     driver.get(e) ##打开地址
#     print("共 "+str(jie_liu_shipinshuliang)+" 个视频，现在处理第："+str(vcount))
#     vcount += 1
#     time.sleep(4)
#
#     for i in range(1,10):##向下滚动
#         driver.execute_script('window.scrollTo(0,'+str(i*500)+')')
#         time.sleep(0.2) 
#
#
#     pl = driver.find_elements(By.CLASS_NAME,'css-1i7ohvi-DivCommentItemContainer')  ##所有的 评论
#
#     time.sleep(1)
#     if pl=="":
#         continue
#     for e in pl:  ## 打印所有评论
#         try:
#             pinglun = e.find_element(By.CLASS_NAME,'css-fx1avz-StyledLink-StyledUserLinkName') ###评论者
#             print(pinglun.get_attribute('href'))
#             print('------------------------------------------')
#             allusers.append(pinglun.get_attribute('href'))
#         except:
#             continue
#
#     time.sleep(5)
# if len(allusers)==0:
#     print("没有匹配到评论")
# i=1
# usermap = {}
# for dyuser in allusers:
#     if dyuser in usermap.keys():
#         continue
#     usermap[dyuser] = dyuser
#     try:
#         ###driver.get("https://www.douyin.com/search/"+str(quote(dyuser))+"?type=user");
#         driver.get(dyuser);
#         time.sleep(6)
#         #uurl = driver.find_element(By.CLASS_NAME,'WTCKzPrM').find_elements(By.CLASS_NAME,'B3AsdZT9')[0].get_attribute("href")
#         #driver.get(uurl)
#         #time.sleep(8)
#
#
#
#
#         b = driver.find_element(By.CLASS_NAME,'css-usq6rj-DivMoreActions')  ## 操作的三个小点
#
#         #print(b[1].text)
#
#         time.sleep(0.5)
#         ac.move_to_element(b).perform() ##鼠标悬停
#         ac.click(b)
#         time.sleep(1)
#         ac.perform()
#
#         sx = driver.find_element(By.CLASS_NAME,'css-i5wukf-PText')   ##找到发消息
#         ac.move_to_element(sx)
#         ac.click(sx)
#         ac.perform()
#         time.sleep(5)
#
#
#
#         t = driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block')   ##新页面找到发消息窗
#         ac.move_to_element(t)
#         ac.click(t)
#         ac.perform()
#         time.sleep(1)
#         print('click over')
#         t.send_keys('1')
#         time.sleep(3)
#         t.send_keys(Keys.ENTER)
#         time.sleep(5)
#         print("共"+str(len(allusers))+"用户，向第"+str(i)+" 个用户："+str(dyuser)+"----发送消息完成")
#         i+=1
#     except:
#         continue