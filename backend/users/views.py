from django.http import HttpResponse
from django.core import serializers
from users.models.models import UserModel
from rest_framework.views import APIView

class User(APIView):
    def get(self, request):
        search = request.GET.get("search","")
        users = []
        if( search != ""):
            users = serializers.serialize("json", UserModel.objects.filter(name__contains=search))
        else:
            users = serializers.serialize("json", UserModel.objects.all())
        return HttpResponse(users, content_type='application/json')
    def post(self, request):
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        name = request.POST.get("name", "")
        if( email is not None and str(email).__len__ > 0):
            return HttpResponse("Preencha o campo de email",status=400,content_type='application/json')
        if( password is not None and str(password).__len__ > 0):
            return HttpResponse("Preencha o campo de senha",status=400, content_type='application/json')
        if( name is not None and str(name).__len__ > 0):
            return HttpResponse("Preencha o campo de nome",status=400, content_type='application/json')
        user = UserModel()
        user.email = email
        user.password = password
        user.name = name
        user.save()
        return HttpResponse("Usuario cadastrado com sucesso")