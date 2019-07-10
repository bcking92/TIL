from datetime import datetime
import random
import bs4
import requests
from flask import Flask


app = Flask(__name__)

# 1. 주문받는 방식(어떻게)

@app.route("/")     

# 2. 무엇을 제공할지(무엇)

def hello():
    return "Hello World!"

'''----------------------------------------------------------'''

@app.route("/hi")           # hi라는 주문이 들어왔을 때 = ip주소/hi
def hi() : 
    return "hi"             # "hi" 를 Return

# 1. /name = 주문서의 이름
# 2. 나의 영문이름

@app.route("/name")
def name1() :
    return "KimByungChul"

@app.route("/hello/<person>")     # <varible name> = varible routing
def hellou(person):               # 함수에 변수명을 입력해준다.
    return "hello, " + person     # hello, 함수값이 페이지에 출력됨.

# /cube/1 ==> 1
# /cube/2 ==> 8
# /cube/3 ==> 27

@app.route("/cube/<num>")
def cube(num):
    
    return str(int(num) ** 3)              # num을 3제곱한 값을 넘겨준다.

# 1. /lotto => 랜덤한 로또 추천 
# 2. /menu => 점심메뉴 추천
# 3. /kospi => 현재 KOSPI 지수 나타내기
# 4. /newyear => 오늘이 1월 1인지 판별

# 1.



@app.route("/lotto")
def lotto() :
    a = list(range(1,46))
    return "LOTTO 추천번호 : " + str(sorted(random.sample(a,6)))[1:len(str(random.sample(a,6)))]

# 2.



@app.route("/menu")
def menu():
    a = ['치킨','돈가스','라면','피자','제육','갈비탕','육개장','편의점']
    return "오늘의 추천 메뉴 : " + str(random.sample(a,1))[1:len(str(random.sample(a,1)))-1]



# 3.

@app.route("/kospi")
def kospi():
    url = "https://finance.naver.com/sise/"
    request = requests.get(url).text
    source = bs4.BeautifulSoup(request, "html.parser")
    kospi = source.select_one("#KOSPI_now")
    return '현재 KOSPI 지수는 ' + str(kospi) + '입니다.'

# 4.

@app.route("/newyear")
def newyear():
    month = datetime.now().month
    day = datetime.now().day
    if month == 1 and day == 1 :
        return "<h1>예</h1>"                # <h1> </h1> 크기조정 태크
    else :
        return "<h1>아니오</h1>"
    # return str(month) + "월" + str(day) + "일"

# /index 이렇게하는건 너무 노가다임
@app.route("/index")
def index():
    return "<html><html></html><body></body><h1>홈페이지</h1><p>이건내용</p></html>"

