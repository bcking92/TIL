import requests
import bs4
# from pprint import pprint
res = requests.get('https://finance.naver.com/sise/').text
doc = bs4.BeautifulSoup(res, 'html.parser')
src = doc.select_one('#siselist_tab_5').text.strip()
                    
print(src)
