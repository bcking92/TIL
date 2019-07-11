from flask import Flask, render_template, request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup


fake = Faker('ko_KR')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/naver/')
def naver():
    return render_template('naver.html')

@app.route('/daum/')
def daum():
    return render_template('daum.html')

@app.route('/pastlife/')
def pastlife():
    return render_template('pastlife.html')

# 이름과 가짜 직업을 알려준다.
storage = {}
@app.route('/result')
def result():
    name = request.args.get('name')
     # Requests랑 다름. 이건 flask가 들고있는것임
    # argument 중에 이름이 name인 변수에 들어있는 것을
    # 가지고 온다.                    
    if name in storage.keys() :
        job = storage[name]
        # 1. 우리 데이터에 해당하는 이름이 있는지 없는지 확인
        # 2. 있다면 => names에 저장된 직업을 보여줌
    else :
        job = fake.job()
        storage[name] = job
        # 3. 없다면 => 랜덤으로 fake 직업을 보여줌, 데이터에 저장
    return render_template('result.html', job = storage[name], name = name)

@app.route('/goonghap')
def goonghap():
    return render_template('goonghap.html')
babo = []

# 변수 + 변수로 dict에 저장했을 때
# storage_cp = {}
# @app.route('/destiny')
# def destiny():
#     person1 = request.args.get('person1')
#     person2 = request.args.get('person2')
#     couple = person1 + person2
#     if couple in storage_cp:
#         love_per = storage_cp[couple]
#     else :
#         love_per = random.choice(range(51,101))
#         storage_cp[couple] = love_per
#     global babo
#     babo.append(person1 + '&' + person2)
#     return render_template('destiny.html', person1 = person1, person2 = person2, love_per = love_per)


# dict in dict 으로 coding 했을때 == 
storage_des = {}
@app.route('/destiny')
def destiny():
    person1 = request.args.get('person1')
    person2 = request.args.get('person2')
    if person1 in storage_des:
        if person2 in storage_des[person1] :
            love_per = storage_des[person1][person2]
        else :
            love_per = random.randint(51,101)
            storage_des[person1][person2] = love_per
    else :
        love_per = random.randint(51,101)
        storage_des[person1] = {person2 : love_per}
    return render_template('destiny.html', person1 = person1, person2 = person2, love_per = love_per)
babos = ''
@app.route('/admin')
def baba():
    for k, v in storage_des.items() :
        for a in v :
            babos = babos + f'{k} ♥ {a}\n' 
    return '바보들 \n'+ babos
    # return render_template('babo.html', babos = babos)


@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def search():
    username = request.args.get('id')
    url = "https://www.op.gg/summoner/userName="+ username
    res = requests.get(url).text
    doc = BeautifulSoup(res, 'html.parser')
    lose = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses").text

    win = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    winr = int(win[0:3])/(int(lose[0:3])+int(win[0:3]))
    if winr < 0.4 :
        msg = "롤을 접으시는 것을 추천합니다."
    elif winr < 0.55 : 
        msg = "롤하면서 스트레스 받으시죠?"
    elif winr < 0.7 :
        msg = "롤좀 하시네요?"
    else :
        msg = "대리하세요?"
    winrate = str(winr * 100) +'%'
    return render_template('search.html', win = win.replace('W','승'), lose = lose.replace('L','패'), username = username, winrate = winrate, msg = msg)

if __name__ == '__main__':
    app.run(debug = True)