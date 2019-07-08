import webbrowser

url = "https://search.daum.net/search?q="

keyword = ["아이유","수지","설현"]

for i in keyword :
    webbrowser.open(url+i)
