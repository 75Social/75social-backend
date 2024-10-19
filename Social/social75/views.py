from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Habit
from .serializer import HabitSerializer
from rest_framework import status


@api_view(['GET'])
def habit_list(request):
    """List all habits or create a new habit"""
    if request.method == 'GET':
        habits = Habit.objects.all()
        serializer = HabitSerializer(habits,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def habit_detail(request,pk):
    """Retrieve, update or delete a habit"""
    try:
        habit = Habit.object.get(pk=pk)
    except Habit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = HabitSerializer(habit)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HabitSerializer(habit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)