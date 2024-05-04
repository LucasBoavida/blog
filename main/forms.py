from django import forms
from django_summernote.widgets import SummernoteWidget

from main.models import *
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Porfolio
        fields = ['titulu','deskrisaun','imajen','statos','enderesu_url']

class ProjectForm(forms.ModelForm):
    data_hahu = forms.DateField(label= 'Data Hahu',widget=DateInput())
    data_remata = forms.DateField(label= 'Data Remata',widget=DateInput())
    class Meta:
        model = Project
        fields = ['portfolio','cat','naran','data_hahu','data_remata','status']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['naran']

class PostForm(forms.ModelForm):
    content = forms.CharField(
        label="konteudu",
        required=False,
        widget=SummernoteWidget(
            attrs={'summernote' : {'width': '100%', 'height': '500px'}}
        )
    )
    category = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']  # Specify the fields you want in your form
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Categoria.objects.all()  # Populate the category field with all categories
          
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']