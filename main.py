import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("./chromedriver_mac64/chromedriver")
#모바일로 검색
driver.get('https://m.map.naver.com/')
driver.implicitly_wait(3)

search_box0=driver.find_element('xpath','//*[@id="header"]/header/div[4]/div/div/div/span[1]/input')#검색창 찾기
search_box0.click() #검색창 선택
search_box1=driver.find_element('xpath','//*[@id="ct"]/div[1]/div[1]/form/div/div[2]/div/span[1]/input')#검색창 찾기
search_box1.send_keys('음식점')#검색어 입력
search_box1.send_keys(Keys.RETURN)#검색어 입력후 확인
time.sleep(5)#데이터 로딩 시간까지 기달리기


html = driver.page_source
soup = BeautifulSoup(html,"html.parser")#html 코드로 bs4 사용
#가계이름 /selctor로 사용
text=soup.select_one("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview > div > strong").string
print(text)

#위치 정보
location_box=driver.find_element('xpath','//*[@id="ct"]/div[2]/ul/li[1]/div[1]/div[1]/div/a/i')#주소 확장을 위한 버튼 찾기
location_box.click() #버튼 클릭
#도로명 주소 / selctor로 사용
text=soup.select_one("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > div.wrap_bx_address._addressBox > div > p:nth-child(1)").string
print(text)

#지번 주소 / selctor로 사용
html_side=soup.select_one("#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > div.wrap_bx_address._addressBox > div > p:nth-child(2)")
html_side.find('span').decompose()#지번 보조 태그 span 삭제
print(html_side.string)


input()#waiting 코드