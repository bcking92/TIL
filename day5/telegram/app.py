from flask import Flask, render_template, request
import requests
import json
from pprint import pprint
from decouple import config
from bs4 import BeautifulSoup


token_url = config('TELEGRAM_TOKEN')
# methods = 'getupdates'
app = Flask(__name__)
msg = None

@app.route('/')
def home():
    global msg
    msg = request.args.get("msg")
    if msg != None :
        base_url = 'https://api.telegram.org/'
        
        method_url = 'sendMessage'                                                                      
        chat_id = '843723954'
        
        url = '{0}bot{1}/{2}?chat_id={3}&text={4}'.format(base_url,token_url,method_url,chat_id,msg)
        requests.get(url)
        return render_template('home.html')
    else :
        return render_template('home.html')

@app.route(f'/{token_url}', methods = ['POST'])
def webhook():
    # 1. 메아리 챗봇
    # (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    # (2) 그대로 전송
    base_url = 'https://api.telegram.org/'
    res = request.get_json()
    chat_id = res.get('message').get('chat').get('id')
    text = res.get('message').get('text')
    if  res.get('message').get('photo') is not None:
        file_id = res.get('message').get('photo')[-1].get('file_id')
        file_res = requests.get(f"{base_url}bot{token_url}/getFile?file_id={file_id}")
        file_path = file_res.json().get('result').get('file_path')
        file_url = f"{base_url}file/bot{token_url}/{file_path}"   
    
        image = requests.get(file_url, stream = True)

        url = "https://openapi.naver.com/v1/vision/celebrity"

        headers = {
                'X-Naver-Client-Id' : config('NAVER_ID'),
                'X-Naver-Client-Secret' : config('NAVER_SECRET')
        }       
        files = {
            'image': image.raw.read()
        } 

        clova_res = requests.post(url, headers = headers, files = files)
        text = str(clova_res.json().get('faces')[0].get('celebrity').get('confidence')) +'% ' + clova_res.json().get('faces')[0].get('celebrity').get('value') +'입니다.'
        method = 'sendMessage'
        url3 = f'{base_url}bot{token_url}/{method}?chat_id={chat_id}&text={text}' 
        requests.get(url3)

    else:
        if text[-3:len(text)] == '영어로' :
            url = "https://openapi.naver.com/v1/papago/n2mt"
            headers = {
                'X-Naver-Client-Id' : config('NAVER_ID'),
                'X-Naver-Client-Secret' : config('NAVER_SECRET')
            }
            data = {
                'source' : 'ko' ,
                'target' : 'en',
                'text' : text[:-3]
                        }
            res = requests.post(url, headers = headers, data = data).json()           
            trslted = res.get('message').get('result').get('translatedText')
            method = 'sendMessage'
            url1 = f'{base_url}bot{token_url}/{method}?chat_id={chat_id}&text={trslted}' 
            requests.get(url1)

        elif text == '식단' :
            text = 'http://edu.ssafy.com/data/upload_files/namo/images/000004/20190708082304576_18S6XNQP.png'
            method = 'sendMessage'
            url0 = f'{base_url}bot{token_url}/{method}?chat_id={chat_id}&text={text}' 
            requests.get(url0)
        else :
            
            method = 'sendMessage'
            url0 = f'{base_url}bot{token_url}/{method}?chat_id={chat_id}&text={text}' 
            requests.get(url0)
    return '',200

if __name__ == '__main__' :
    app.run(debug=True)