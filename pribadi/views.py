from django.shortcuts import render
from . models import *
# Create your views here.
def Dashboard(request):
 data = Profil.objects.all()

 web = Portfolio.objects.filter(kategori='web_dev').first()
 cd = Portfolio.objects.filter(kategori='creative_design').first()
 # gd = Portfolio.objects.filter(kategori='graphic_design').first()

 program = Portfolio.objects.all()


 dj = {
  'd' : data,
  '1' : web,
  '2' : cd,
  # '3' : gd,
  'p' : program,
  'title' : 'My Profile | Portfolio',
 }
 return render(request, 'Index.html', dj)