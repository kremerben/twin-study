import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def test_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # deleteMe = Movie.objects.get(title=data).delete()

        return HttpResponse(json.dumps(data), content_type='application/json')
        # return render_to_response('movie_template.html', movie_info)
