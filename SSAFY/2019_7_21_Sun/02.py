from datetime import datetime, date, timedelta
import decouple
import requests
import json
from pprint import pprint
import csv

base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
kopis_key = decouple.config('KOBIS_KEY')
movies_details = []
with open('boxoffice.csv', 'r', encoding = 'utf-8') as f:
    a = f.readlines()
    for i in range(1,len(a)):
        movie_info = {}
        movieCd = a[i][:8]
        url = f'{base}?key={kopis_key}&movieCd={movieCd}'
        res = requests.get(url).json()
            
        movie_info['영화대표코드'] = res.get('movieInfoResult').get('movieInfo').get('movieCd')
        movie_info['영화명(국문)'] = res.get('movieInfoResult').get('movieInfo').get('movieNm')
        movie_info['영화명(영문)'] = res.get('movieInfoResult').get('movieInfo').get('movieNmEn')
        movie_info['영화명(원문)'] = res.get('movieInfoResult').get('movieInfo').get('movieNmOg')
        movie_info['제작년도'] = res.get('movieInfoResult').get('movieInfo').get('prdtYear')
        movie_info['개봉일'] = res.get('movieInfoResult').get('movieInfo').get('openDt')
        movie_info['장르'] = list(res.get('movieInfoResult').get('movieInfo').get('genres')[0].values())[0]
        
        try:
            movie_info['감독명'] = list(res.get('movieInfoResult').get('movieInfo').get('directors')[0].values())[0]
        except:
            movie_info['감독명'] = '정보없음'

        try:
            movie_info['관람등급'] = res.get('movieInfoResult').get('movieInfo').get('audits')[0].get('watchGradeNm')
        except:
            movie_info['관람등급'] = '정보없음'

        movies_details.append(movie_info)
        print(i)

with open('movie.csv', 'w', encoding='utf-8',newline='') as f:
    fieldnames = ['영화대표코드','영화명(국문)','영화명(영문)','영화명(원문)','제작년도','개봉일', '장르','감독명','관람등급']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for movie in movies_details:
        writer.writerow(movie)
    



# movieCd,movieNm,movieNmEn,movieNmOg,prdtYear,showTm,openDt,genreNm,peopleNm,peopleNmEn,audits