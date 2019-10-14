from django import forms

# model이랑 비슷함.
# form 태그를 많이쓰니까 이걸 model이랑 연동해서 모듈화 시키겟다 이말이야
class ArticleForm(forms.Form):
    # forms.field를 통해 사용자로 부터 받는 데이터를 핸들링할 것임
    # 사용자는 뭔짓을할지 모른다. 항상 통제해야됨
    # 유효성검사. 사용자가 뭔짓을해도 오류가 안나게 데이터를 검증하는 것
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    required_css_class = 'required'
