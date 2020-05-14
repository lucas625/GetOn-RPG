from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models.models import UserModel
import json

@csrf_exempt
def index(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        name = request.POST.get("name", "")
        if( email == ""):
            return HttpResponse("Preencha o campo de email",status=400)
        if( password == ""):
            return HttpResponse("Preencha o campo de senha",status=400)
        if( name == ""):
            return HttpResponse("Preencha o campo de nome",status=400)
        user = UserModel()
        user.email = email
        user.password = password
        user.name = name
        user.save()
        return HttpResponse("Usuario cadastrado com sucesso")
    if request.method == "GET":
        search = request.GET.get("search","")
        users = []
        if( search != ""):
            users = serializers.serialize("json", UserModel.objects.filter(name__contains=search))
        else:
            users = serializers.serialize("json", UserModel.objects.all())
        return HttpResponse(users, content_type='application/json')
    if request.method == "PUT":
        return HttpResponse("Get user routes")
    return HttpResponse("Hello, world. You're at the polls index.")

    