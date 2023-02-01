from django.forms import ModelForm
from git_fork.models import Github


class GithubForm(ModelForm):
    class Meta:
        model = Github 
        fields = '__all__'
        # placeholders = ['github account name', 'new repo name', 'your github bearer token']
