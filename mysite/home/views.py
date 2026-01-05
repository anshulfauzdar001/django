from django.shortcuts import render

from django.http import HttpResponse




def home(request):
  people=[{"name": "anshul" , "age": 19} , 
        {"name": "varshit" , "age": 21},]
  return render(request, "index.html" , {'people': people})
