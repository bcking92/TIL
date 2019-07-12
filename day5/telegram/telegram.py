import requests
from decouple import config
## url을 변경가능한 단위로 쪼개서 각각 다른변수로 저장해 놓는것이 좋음. 다른 사람들도 코드를 이해할 수 있게.
base_url = 'https://api.telegram.org/'
token_url = config("TELEGRAM_TOKEN")
print(token_url)
method_url = 'sendMessage'                                                                      
chat_id = '843723954'
text = 'gdgd'
url = '{0}{1}{2}?chat_id={3}&text={4}'.format(base_url,token_url,method_url,chat_id,text)
res = requests.get(url)

print(res.text)