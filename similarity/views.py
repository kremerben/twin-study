import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import requests


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


