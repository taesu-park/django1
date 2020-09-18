from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, 
    error_messages={
        'required': '이름을 입력해주세요.'
    },
    label="사용자이름")
    password = forms.CharField(widget=forms.PasswordInput, 
    error_messages={
        'required': '비밀번호를 입력해주세요.'
    }
    ,label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = User.objects.get(username=username)
            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else:
                self.user_id = user.id
                
                  
