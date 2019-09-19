from django import forms
from django.forms import widgets

from apps.user_profile.models import UserModel


class RegistrationForm(forms.ModelForm):
    password_again = forms.CharField(max_length=128, widget=forms.PasswordInput())

    class Meta:
        model = UserModel

        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'date_birth',
            'username',
            'password',
            'password_again'
        ]

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        """
        Check password for correct repeat

        :return: str, password
        """
        if self.cleaned_data['password'] != self.cleaned_data['password_again']:
            raise forms.ValidationError('Are you stupid?')
        return self.data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.slug = self.cleaned_data['username']
        user.save()
        return user
