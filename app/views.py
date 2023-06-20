from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

# Create your views here.

from .models import Home,AboutUs,Contact,Icon,Carusel


# View metodida - 2xil usul bor


# 1) Agar html fayllar bittani ichida ishlailsa - index funksiya metodidan foydalaniladi

# 2) Agar html fayl ko'p bo'lsa - ListView klasslik metoddan foydalanamiz


# class PortfoliyomViews(ListView):
#     model = Portfolio
#     context_object_name = 'portfolio'
#     template_name = 'index.html'

def index(request):
    home = Home.objects.all()
    aboutus = AboutUs.objects.all()
    contact = Contact.objects.all()
    icon = Icon.objects.all()
    carusel = Carusel.objects.all()





    contex = {
        'Home': home,
        'Aboutus':aboutus,
        'Contact':contact,
        'Icon':icon,
        'Carusel':carusel,


    }
    return render(request, ['index.html'], contex)
    return render(request, 'index.html')

