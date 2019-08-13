from django.shortcuts import render
import requests

font_res = requests.get('http://artii.herokuapp.com/fonts_list').text.split('\n')

# Create your views here.
def artii(request):
    return render(request, 'artii/artii.html', {'font_res' : font_res})

def result(request):

    import random
    word = request.POST.get('word')
    font = request.POST.get('font')
    url = f'http://artii.herokuapp.com/make?text={word}&font={font}'
    res = requests.get(url).text
    context = {
        'res' : res,
    }
    return render(request, 'artii/result.html', context)