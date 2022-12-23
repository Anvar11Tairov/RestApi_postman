from django.shortcuts import render
from .models import MyUsers
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.forms.models import model_to_dict

class UsersApiView(APIView):

    def get(self, request):
        data = MyUsers.objects.all().values()
        return Response(list(data))

    def post(self, request):
        new_user = MyUsers(name = request.data['name'], age = request.data['age'])
        new_user.save()
        return Response(model_to_dict(new_user))

    def put(self, request):
        put_user = MyUsers(id = request.data['id'],
                              name = request.data['name'],
                                  age = request.data['age'])
        put_user.save()
        return Response(model_to_dict(put_user))

    def delete(self, request):
        delete_user = MyUsers(id = request.data['id'],
                                 name = request.data['name'],
                                      age = request.data['age'])
        delete_user.delete()
        return Response(model_to_dict(delete_user))
class Users_Id(APIView):
    def get(self, request, id):
        data =  MyUsers.objects.get(id=id)
        return  Response(model_to_dict(data))

