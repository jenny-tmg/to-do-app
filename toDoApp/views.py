from django.shortcuts import reader 
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET", "POST"])
def todo_list(request):
    if request.method == "GET":
        todos = ToDo.objects.all()
        seriallizer = ToDoSerializer(todos , many = True)
        return Response(seriallizer.date)
    
    elif request.method =="POST":
        seriallizer = ToDoSerializer("data = request.data")
        if seriallizer.is_valid():
            seriallizer.save()
            return Response(seriallizer.data, status= status.HTTP_201_CREATED)
        return Respone(seriallizer.error, status = status.HTTP_404_BAD_REQUEST)