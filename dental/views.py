from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "dental/index.html")

def service(request):
    return render(request, "dental/service.html")
