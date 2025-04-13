from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label = "Имя", help_text="введите ваше имя")
    age = forms.IntegerField(label = "Возраст")
    sex = forms.ChoiceField(
        choices=[
            ('Man', 'Мужской'),
            ('Woman', 'Женский'),
        ],
        widget=forms.RadioSelect,
        label = "Ваш пол: "
    )
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)

class Registration(forms.Form):
    login = forms.CharField(label="Логин", help_text="Введите логин")
    password = forms.CharField(label="password", help_text="Введите возраст")

