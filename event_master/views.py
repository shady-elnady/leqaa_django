from django.shortcuts import render, redirect


# Create your views here.


app_templete_pages = "event_master/pages"


def index(request):
    return render(request, f"{app_templete_pages}/index.html")


def about(request):
    return render(request, f"{app_templete_pages}/about.html")


def spakers(request):
    return render(request, f"{app_templete_pages}/spakers.html")


def schedule(request):
    return render(request, f"{app_templete_pages}/schedule.html")


def blog(request):
    return render(request, f"{app_templete_pages}/blog.html")


def blog_details(request):
    return render(request, f"{app_templete_pages}/blog_details.html")


def contact(request):
    return render(request, f"{app_templete_pages}/contact.html")


def elements(request):
    return render(request, f"{app_templete_pages}/elements.html")


def splash(request):
    return render(request, f"{app_templete_pages}/splash.html")
