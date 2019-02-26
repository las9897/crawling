from bs4 import BeautifulSoup
import requests


def spider():
        url="http://www.naver.com/"
        srcCode = requests.get(url)
        plainText = srcCode.text
        soup = BeautifulSoup(plainText, 'lxml')
        rank_list =[]
        for rank in soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a'):
            rank_list.append({'rank': rank.find_all("span")[0].text, 'data':rank.find_all("span")[1].text, 'link':rank.get('href')})

        for rank_data in rank_list:
            print(rank_data['rank']+"\t" + rank_data['data']+"\t"+rank_data['link'])

            
        


spider()
