import requests
import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from git_fork.forms import GithubForm


def index(request):
    # template = loader.get_template('git_fork/base.html')
    if request.method == 'POST':
        form = GithubForm(request.POST)
        if form.is_valid():
            account = form.data['account']  # the github account to fork FROM
            repo = form.data['repo']  # the github account to fork TO your account
            new_repo = form.data['new_repo'] if not None else repo  # the name of the repo on your account
            your_account = form.data['your_account']  # your github account user name
            token = form.data['token']
            url = f'https://api.github.com/repos/{account}/{repo}/forks'
            payload = json.dumps({"name": new_repo, "default_branch_only": True})
            headers = {
                        'content-type': 'application/json',
                        'Accept-Charset': 'UTF-8',
                        "Accept": "application/vnd.github+json",
                        "Authorization": f"Bearer {token}",
                        "X-GitHub-Api-Version": "2022-11-28",
                    }
            r = requests.post(url, data=payload, headers=headers)
            if r.status_code == 202:
                form.save()
                link = f"https://github.com/{your_account}/{new_repo}"
                return HttpResponse("<h1>SUCCESS!</h1><a href='" + link + "'>" + link + "</a>")
            else:
                return HttpResponse("failed")
            # perform some action and return a success response
    else:
        form = GithubForm()

    return render(request, 'git_fork/base.html', {'form': form})
