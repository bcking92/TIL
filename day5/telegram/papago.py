# 파파고 API 쓰는방법
import requests
from decouple import config
from pprint import  pprint


url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id' : config('NAVER_ID'),
    'X-Naver-Client-Secret' : config('NAVER_SECRET')
}
data = {
    'source' : 'ko' ,
    'target' : 'en',
    'text' : '댕댕이'
}


res = requests.post(url, headers = headers, data = data).json()           
trslted = res.get('message').get('result').get('translatedText')
pprint(trslted)


# 데이터를 보낼 때 post()를 사용 특히 데이터가