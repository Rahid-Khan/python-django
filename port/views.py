from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def app(request):
    return HttpResponse('this the page of the app')

def detail(request, question_id):
    return HttpResponse('you are looking at the question '% question_id)

def vote(request , question_id):
    return HttpResponse('your voting for the '% question_id)

def results(request, question_id):
    respone = 'the reult of the poll.'
    return HttpResponse( respone % question_id)