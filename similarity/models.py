from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)


class Quiz(models.Model):
    pass


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    weight = models.SmallIntegerField(default=1)
    quiz = models.ForeignKey(Quiz, related_name='quiz')

class Quiz_Response(models.Model):
    # response_text = models.
    pass


