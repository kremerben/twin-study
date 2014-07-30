from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.contenttypes import generic

from domande.models import Question, Answer

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)

class Questionnaire(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)
