from datetime import datetime, date, timedelta
import decouple
import requests
import json
from pprint import pprint
import csv

base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
kopis_key = decouple.config('KOBIS_KEY')
features = ['peopleCd','peopleNm','repRoleNm','filmoNames']
director = []
with open('movie.csv', 'r', encoding = 'utf-8') as f:
    a = f.readlines()
    for i in range(1,len(a)):
        dir_name = a[i].strip().split(',')[-2].replace(' ','%20')
        print(dir_name.replace(' ','%20'))
        url = f'{base}?key={kopis_key}&peopleNm={dir_name}'
        res = requests.get(url).json()
        for i in range(len(res.get('peopleListResult').get('peopleList'))):
            instantdict = {}
            if res.get('peopleListResult').get('peopleList')[i].get('repRoleNm') == '감독':
                for feature in features:
                    try:
                        instantdict[feature] = res.get('peopleListResult').get('peopleList')[i].get(feature)                    
                    except:
                        instantdict[feature] = '정보없음'
            else:
                continue
            director.append(instantdict)
            pprint(instantdict)

with open('director.csv', 'w', encoding = 'utf-8', newline='') as f:
    fieldnames = ['peopleCd','peopleNm','repRoleNm','filmoNames']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(director)):
        writer.writerow(director[i])
    


# # peopleCd,peopleNm,repRoleNm,filmoNames