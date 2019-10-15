from django import forms
from .models import Article, Comment
# model이랑 비슷함.
# form 태그를 많이쓰니까 이걸 model이랑 연동해서 모듈화 시키겟다 이말이야
# class ArticleForm(forms.Form):
    # forms.field를 통해 사용자로 부터 받는 데이터를 핸들링할 것임
    # 사용자는 뭔짓을할지 모른다. 항상 통제해야됨
    # 유효성검사. 사용자가 뭔짓을해도 오류가 안나게 데이터를 검증하는 것

    # title = forms.CharField(
    #     max_length=20,
    #     label='title',
    #     help_text='제목은 20자를 넘길 수 없습니다.',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control my-content',
    #             'placeholder': '제목을 입력해주세요',
    #         }
    #     ) 
    # )
    # content = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #             'class': 'form-control my-content',
    #             'placeholder': '내용을 입력해주세요',
    #             'rows': 5,
    #             'cols': 50,
    #         }
    #     )
    # )
    # required_css_class = 'required'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        # exclude = ('title',) <- '얘는 폼으로 안만들래~' 하는것이다.
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control my-content',
                    'placeholder': '제목을 입력해줴요',
                }),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control my-content',
                    'placeholder': '내용을 입력해주쎄용',
                    'rows': 5,
                    'cols': 5,
                })
        }
    title = forms.CharField(
        max_length=20,
        label='title',
        help_text='제목은 20자를 넘길 수 없습니다.',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control my-content',
                    'placeholder': '제목을 입력해줴요',
            }
        )
    )
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
    
    comment = forms.CharField(
        label='',
    )
    