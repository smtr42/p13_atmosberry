from django.shortcuts import render

def frontpage(request):
    return render(request, "frontend/templates/index.html")