from datetime import datetime, date, timedelta
import decouple
import requests
import json
from pprint import pprint
import csv

base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
kopis_key = decouple.config('KOBIS_KEY')

box_top10_weekly = {}
# for weeksago in list(range(50))[::-1]:
#     targetDt = str(date.today() - timedelta(weeks = 1 + weeksago)).replace('-','')
#     url = f'{base}?key={kopis_key}&targetDt={targetDt}&weekGb=0&itemPerPage=10'
#     res = requests.get(url).json()
#     for rank in range(0,10):
#         movie_name = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('movieNm')
#         movie_Cd = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('movieCd')
#         movie_audiAcc = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('audiAcc')
#         movie_showRange = res.get('boxOfficeResult').get('showRange')
#         if movie_name in box_top10_weekly:
#             if int(movie_audiAcc) >= int(box_top10_weekly.get(movie_name).get('movie_audiAcc')):
#                 box_top10_weekly[movie_name] = {'movie_Cd' : movie_Cd, 'movie_audiAcc' : movie_audiAcc, 'showRange' : movie_showRange[-8:]}
#             else:
#                 continue
#         else:
#             box_top10_weekly[movie_name] = {'movie_Cd' : movie_Cd,'movie_audiAcc' : movie_audiAcc, 'showRange' : movie_showRange[-8:]}

for weeksago in list(range(50))[::-1]:
    targetDt = str(date.today() - timedelta(days = 6) - timedelta(weeks = weeksago)).replace('-','')
    url = f'{base}?key={kopis_key}&targetDt={targetDt}&weekGb=0&itemPerPage=10'
    res = requests.get(url).json()
    for rank in range(0,10):
        movie_name = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('movieNm')
        movie_Cd = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('movieCd')
        movie_audiAcc = res.get('boxOfficeResult').get('weeklyBoxOfficeList')[rank].get('audiAcc')
        movie_showRange = res.get('boxOfficeResult').get('showRange')
        if movie_Cd in box_top10_weekly:
            if int(movie_audiAcc) >= int(box_top10_weekly.get(movie_Cd).get('movie_audiAcc')):
                box_top10_weekly[movie_Cd] = {'movie_Cd' : movie_Cd ,'movie_name' : movie_name, 'movie_audiAcc' : movie_audiAcc, 'showRange' : movie_showRange[-8:]}
            else:
                continue
        else:
            box_top10_weekly[movie_Cd] = {'movie_Cd' : movie_Cd , 'movie_name' : movie_name,'movie_audiAcc' : movie_audiAcc, 'showRange' : movie_showRange[-8:]} 

pprint(box_top10_weekly)


with open('boxoffice.csv', 'w', encoding='utf-8',newline = '') as f:
    fieldnames = ['movie_Cd','movie_name','movie_audiAcc','showRange']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for movie_Cd in box_top10_weekly:
        writer.writerow(box_top10_weekly.get(movie_Cd))
    

# 영화대표코드 = movieCd 영화명 = movieNm
# 해당일 누적관객수 = audiAcc 조회일자 = showRange