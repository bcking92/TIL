from flask import Flask, render_template
import requests
import datetime
import bs4
import random


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')         # template을 통해 html 문서를 불러오는데 file 이름을 설정

@app.route("/hello/<name>")
def hello(name):
    # name에는 /hello/이름/ <-활용가능
    return render_template('Hello.html', name = name)        # html 템플릿에 파이썬 코드를 넣어서 렌더링하려고함

@app.route('/menu/')
def menu():
    # 랜덤으로 음식 메뉴를 추천하고
    # 해당 음식 사진을 보여주는 기능을 구현
    menu = {'치킨': 'https://www.mpps.co.kr/kfcs_api_img/KFCS/goods/DL_2172964_20181218164342743.png' ,
     '짜장면' :'http://ojsfile.ohmynews.com/STD_IMG_FILE/2017/0427/IE002151398_STD.JPG',
     '돈까스' : 'https://cdn.clien.net/web/api/file/F01/7420963/213bd93166374f.jpg',
      '제육': 'https://mblogthumb-phinf.pstatic.net/20140916_154/dew36_14107988004269WVlb_JPEG/1.jpg?type=w2' , 
      '초밥' : 'http://mblogthumb2.phinf.naver.net/MjAxNzAzMDZfOTUg/MDAxNDg4ODA2NzYxMjMy.GBaA7LWRZtgAQDxkWD47_quKGTGR0gJCvCRVDh8xBbMg.p4Smgay1gtqeXjP2i15vSdjb7WrLwRw5Ucyf65dCR7Ag.JPEG.boru130/DSC08901.JPG?type=w800'}
    selected = random.choice(list(menu.keys()))
    return render_template('menu.html', foodname = selected, foodimage = menu[selected])



# /lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능

@app.route('/lotto/')
def lotto():
    no_lotto = 866
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={no_lotto}"
    request = requests.get(url)
    dict_lotto = request.json()
    your_lotto = sorted(random.sample(range(1,46),6))
    # your_lotto = [9,29,34,37,39,12]
    winner = []
    for i in range(1,7):
        winner.append(dict_lotto[f'drwtNo{i}'])
    count = len(set(your_lotto) & set(winner))
    if count == 6 :
        a = '1등이십니다.ㄷㄷㄷㄷ'
    elif count == 5 :
        second_winner = winner
        second_winner.append(dict_lotto[f'bnusNo'])
        if len(set(your_lotto) & set(second_winner)) == 6:
            a = '2등이십니다.ㄷㄷ'
        else :
            a = '3등이십니다. ㅊㅋㅊㅋ'
    elif count == 4 :
        a = '4등이십니다. ㅊㅊ'
    elif count == 3 :
        a = '5등이십니다. ㅅㅅ'
    else :
        a = '꽝입니두'
    return render_template('lotto.html', 
    win_or_not = a, 
    your_lotto = str(your_lotto)[1:len(str(your_lotto))-1], 
    winner = str(winner)[1:len(str(winner))-1])
    
    

# flask를 다시돌릴필요 없음. 이 코드 이후엔 python app.py로 돌려야함
if __name__ == "__main__" :
    app.run(debug=True)
