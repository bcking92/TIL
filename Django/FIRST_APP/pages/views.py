from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return render_template('index.html')
    # request 를 꼭 넣어줘야댐 request 는 사용자가 보낸 정보임
    return render(request, 'index.html')


def home(request):
    # return HttpResponse('<h1>홈페이지')
    name = '김병철'
    data = ['김병철', '김현호', '따따따']
    empty_data = ['역도산', '성냥팔이소녀의 재림', '오오']
    # 장고는 변수를 넘길 때 딕셔너리 형태로 넘김
    matrix = [[1,2,3],[4,5,6]]
    number = 10
    context = {
        'name' : name,
        'data' : data,
        'empty_data' : empty_data,
        'matrix' : matrix,
        'number' : number,
    }
    return render(request, 'home.html', context)

def lotto(request):
    import random
    lotto = sorted(list(random.sample(list(range(1,46)),6)))
    context = {
        'lotto' : lotto,
    }
    return render(request, 'lotto.html', context)

def cube(request,num):
    result = num ** 3
    context = {
        'result' : result
    }
    return render(request,'cube.html', context)

def match(request):
    import random
    num = random.randint(50,100)
    me = request.POST.get('me')
    you = request.POST.get('you')
    context = {
        'num' : num,
        'me' : me,
        'you' : you,
    }
    return render(request, 'match.html', context)