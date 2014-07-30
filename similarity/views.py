import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import requests
from models import Questionnaire, User
from forms import QuestionnaireForm, SimilarityUserCreationForm, UserForm


def home(request):
    return render(request, 'home.html')


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
        "app_id": "6667e13f",
       "app_key": "a5d5074a84da848f6fab9f0a021a0b93",
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

