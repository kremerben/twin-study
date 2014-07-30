from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.contenttypes import generic

from domande.models import Question, Answer

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)



class Gallery(models.Model):
    gallery_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=True, blank=True)


class UserImage(models.Model):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    subject_id = models.CharField(max_length=50)
    gallery_name = models.ForeignKey(Gallery, related_name='gallery')



class Questionnaire(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)
