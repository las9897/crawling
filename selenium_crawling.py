from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\\Project\\chromedriver.exe')

driver.implicitly_wait(3)
# 암무적으로 웹 자원 로드를 위해 3초까지 기다려준다.

'''
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('las9897')
driver.find_element_by_name('pw').send_keys('@ab1ac4ad7!')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
'''
driver.get('https://blog.naver.com/tech-plus')
#driver.get('https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/')

driver.switch_to.frame('mainFrame')
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
posts = soup.select('html')

#posts = soup.select('#prologue > dl:nth-child(2) > dd:nth-child(1) > ul')


print(posts)

