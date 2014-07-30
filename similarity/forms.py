from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from models import *



class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "image", "username", "password")


class UserImageForm(forms.Form):
    image = forms.ImageField()



class QuestionnaireForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(QuestionnaireForm, self).__init__(*args, **kwargs)
    #
    #     # If you pass FormHelper constructor a form instance
    #     # It builds a default layout with all its fields
    #     self.helper = FormHelper(self)
    #
    #     # You can dynamically adjust your layout
    #     self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Questionnaire


class SimilarityUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "image",  "password1", "password2")

    def clean_username(self):
            # Since User.username is unique, this check is redundant,
            # but it sets a nicer error message than the ORM. See #13147.
            username = self.cleaned_data["username"]
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )

