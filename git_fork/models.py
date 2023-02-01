from django.db import models


class Github(models.Model):
    account = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)
    new_repo = models.CharField(max_length=100)
    your_account = models.CharField(max_length=100)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.account
