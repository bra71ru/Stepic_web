from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from models import Question, Answer, User


#class AskForm(forms.Form):
#    title = forms.CharField(max_length=255)
#    text = forms.CharField(widget=forms.Textarea)
#
#    def save(self):
#        question = Question(**self.cleaned_data)
#        question.save()
#        return question

class AskForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title','text']


class AnswerForm(ModelForm):

    class ModelChoiceField_title(forms.ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.title

    question = ModelChoiceField_title(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['question','text']


class SignupForm(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):

    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    error_messages = {
        'invalid_login': "Please enter a correct username and password.",
        'inactive': "This account is inactive.",
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user:
                if self.user.is_active:
                    return self.cleaned_data
                else:
                    raise forms.ValidationError(
                        self.error_messages['inactive'],
                        code='inactive',
                        )
        raise forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            )

    def get_user(self):
        return self.user
