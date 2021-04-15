from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'projects/home.html')

def about(request):
    return render(request, 'projects/about.html')

def gallery(request):
    return render(request, 'projects/gallery.html')

def news(request):
    return render(request, 'projects/news.html')

def contact(request):
    return render(request, 'projects/contact.html')