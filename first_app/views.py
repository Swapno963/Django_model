from django.shortcuts import render
from . import models
# Create your views here.
def home(response):
    student = models.Student.objects.all()
    return render(response,'index.html', {'data':student})