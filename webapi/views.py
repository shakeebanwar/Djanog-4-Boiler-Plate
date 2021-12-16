from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from passlib.hash import django_pbkdf2_sha256 as handler
from webapi.models import *
# Create your views here.


class crud(APIView):
    def get(self,request):
        data = Super_AdminAccount.objects.values('SId','Fname','Lname','Email','Username','Role','Profile')
        return Response({'status':True,'data':data})
      

    def post(self,request):
        
        fname = request.data['Fname']
        lname = request.data['Lname']
        email = request.data['Email']
        username = request.data['Username']
        password = handler.hash(request.data['Password'])
        contact = request.data['ContactNo']
        role = request.data['Role']
        profile = request.data['Profile']
        data = Super_AdminAccount(Fname = fname,Lname = lname,Email = email,Username = username,Password = password,ContactNo =contact,Role = role,Profile = profile)
        data.save()
        return Response({'status':True,'message':"save successfully"})




