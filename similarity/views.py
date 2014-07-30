import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import requests
from models import Questionnaire, User, Gallery, UserImage
from forms import QuestionnaireForm, SimilarityUserCreationForm, UserForm, UserImageForm
# from settings import *
from django.conf import settings


def home(request):
    return render(request, 'home.html')


@login_required
def add_image(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            subject_id = request.user.first_name
            gallery_name = request.user.last_name
            gallery, created = Gallery.objects.get_or_create(gallery_name=gallery_name, user=request.user)
            image = UserImage.objects.create(image=image, subject_id=subject_id, gallery_name=gallery)

            return redirect("/view_gallery/")
    else:
        form = UserImageForm()
    data = {"user": request.user, "form": form}
    return render(request, "gallery/add_image.html", data)


@login_required
def profile_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)







@login_required
def view_gallery(request):
    gallery = Gallery.objects.get(user=request.user)
    images = UserImage.objects.filter(gallery_name=gallery)
    data = {
        'user': request.user,
        'images': images,
    }
    return render(request, 'gallery/view_gallery.html', data)



@csrf_exempt
def test_post(request):
    json_data = request.POST.get('app_id', False)
    url = "http://api.kairos.io/enroll"
    payload = {
        "url": "http://dev.kremerdesign.com/twin_study/images/1.jpg",
        "subject_id": "Ben1",
        "gallery_name": "Kremer"
    }
    headers = {
        "app_id": settings.KAIROS_APP_ID,
       "app_key": settings.KAIROS_API_KEY,
        "Accept": "*/*",
        "Content-Type": "application/json",
        "contentType": "application/json"
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)

    # if request.method == 'POST':
    #     data = json.loads(request.body)
        # deleteMe = Movie.objects.get(title=data).delete()

    return HttpResponse(json_data, content_type='text')
        # return render_to_response('movie_template.html', movie_info)



def questionnaire_view(request):
    questionnaire = Questionnaire.objects.get(id=1)

    forms = [q.get_form()(prefix=str(q.id),
                content_object=request.user,
                question=q, form_tag=False)
                   for q in questionnaire.questions.all().get_real_instances()
               ]
    return render(request, "questionnaire.html", forms)


def questionnaire_view111(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/")
    else:
        form = QuestionnaireForm()
    return render(request, "questionnaire.html", {
        'form': form,
    })




def save_view(request, questionnaire):
    # for sake of example use .get
    questionnaire = Questionnaire.objects.get(id=questionnaire)

    forms = [q.get_form()(request.POST or None,
                prefix=str(q.id),
                content_object=request.user,
                question=q, form_tag=False)
                    for q in questionnaire.questions.all().get_real_instances()
            ]

    forms_are_valid = []

    for form in forms:
        forms_are_valid.append(valid)
        valid = form.is_valid()
        if valid:
            t = form.save()

    forms_are_valid = all(forms_are_valid)




"""
USER PROFILES
"""

def register(request):
    if request.method == 'POST':
        form = SimilarityUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("profile")
    else:
        form = SimilarityUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    data = {
        'user': request.user,
    }
    return render(request, 'profile/profile.html', data)


@login_required
def profile_update(request, user_id):
    if int(request.user.id) != int(user_id):
        return redirect("profile")
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)

