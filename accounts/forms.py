from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile ,Education,Endorsement,Workexp,Projects


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

#in order to update profile we will use inbuilt ModelForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email']

#inorder to update profile we will make another class
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','profession','birthdate','position','about','phone_number','address',
        'facebook','linkedin','twitter']

class ProfileUpdateForma(forms.ModelForm):
    class Meta:        
        model = Education
        fields = ['institute' , 'start_date' , 'end_date']

class ProfileUpdateFormb(forms.ModelForm):
    class Meta:
        model = Workexp
        fields = ['company_name' ,'work_descp' , 'start_date' , 'end_date']

class ProfileUpdateFormc(forms.ModelForm):
    class Meta:        
        model = Projects
        fields = ['project_name' ,'project_descp' , 'start_date' , 'end_date']

class ProfileUpdateFormd(forms.ModelForm):
    class Meta:
        model = Endorsement
        fields = ['comment' ,'created_date', 'approved_comment']
        
