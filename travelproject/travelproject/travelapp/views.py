from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import meet
def demo(request):
   obj=place.objects.all()
   ob=meet.objects.all()
   return render(request,"index.html",{'result':obj,'res':ob})

