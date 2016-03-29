from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request, num1, num2):
    return HttpResponse(num1 + ' + ' + num2 + ' = ' + str(int(num1)+int(num2)))

def sub(request, num1, num2):
    return HttpResponse(num1 + ' - ' + num2 + ' = ' + str(int(num1)-int(num2)))

def mul(request, num1, num2):
    return HttpResponse(num1 + ' * ' + num2 + ' = ' + str(int(num1)*int(num2)))

def div(request, num1, num2):
    return HttpResponse(num1 + ' / ' + num2 + ' = ' + str(int(num1)/int(num2)))
