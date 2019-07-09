import requests
import bs4

src_url = "https://www.naver.com"

src_response = requests.get(src_url).text

src_document = bs4.BeautifulSoup(src_response, "html.parser" )

src = src_document.select(".ah_k",limit = 10)

for i in range(len(src)):
    print("인기검색어",i+1,"위는 " + src[i].text +"입니다")


##############################

ex_url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"

ex_response = requests.get(ex_url).text

ex_document = bs4.BeautifulSoup(ex_response, "html.parser")

ex_rate = ex_document.select_one(".usd > div:nth-child(2) > span:nth-child(1)").text

print("현재 원/달러 환율은 " + ex_rate + "입니다")

################################################

url0 = "https://finance.naver.com/sise/"

response = requests.get(url0).text

document = bs4.BeautifulSoup(response, 'html.parser')

kospi = document.select_one("#KOSPI_now").text

kosdaq = document.select_one("#KOSDAQ_now").text

kospi200 = document.select_one("#KPI200_now").text

print("현재 KOSPI 지수는 " + kospi + "입니다")
print("현재 KOSDAQ 지수는 " + kosdaq + "입니다")
print("현재 KOSPI200 지수는 " + kospi200 + "입니다")

