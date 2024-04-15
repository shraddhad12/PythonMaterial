from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World')
    return render(request, 'hey.html', {'name': 'Sourabh', 'message': 'I love you'})

