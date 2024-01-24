from django.shortcuts import render, redirect
from .models import EmpRegistration,EmpDetails
from .forms import EmpRegistrationForm
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.views import APIView
from employee_registration.serializer import *

def registration_list(request):
    content = {'registration_list': EmpRegistration.objects.all()}
    return render(request, 'registration/employee_list.html', {'content': content})

def registration_create(request):
    if request.method == 'POST':
        form = EmpRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = EmpRegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})

def registration_delete(request, id):
    if request.method == 'POST':
        emp_registration = EmpRegistration.objects.get(pk=id)
        emp_registration.delete()
        return redirect('registration_list')
    else:
        # You may want to add error handling here or redirect to an error page
        pass


class EmpDetailsList(viewsets.ModelViewSet):
    serializer_class=EmpDetailsSerializer
    queryset=EmpDetails.objects.all()

    def post(self,request):
        empSerializerObj=EmpDetailsSerializer(data=request.data)
        if empSerializerObj.is_valid():
            empSerializerObj.save()
            return Response(200)
        return Response(EmpDetailsSerializer.errors)
    

    def update(self,request,*args,**kwargs):
        instance=self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(instance)
        return Response(status=status.HTTP_200_OK)
    


class PositionList(viewsets.ModelViewSet):
    serializer_class=PositionSerializer
    queryset=Position.objects.all()


class CommentList(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

    def post(self,request):
        serializerObj=CommentSerializer(data=request.data)
        if serializerObj.is_valid():
            serializerObj.save()
            return Response(200)
        return Response(CommentSerializer.errors)
    



# class ShopingCheckoutList(viewsets.ModelViewSet):


