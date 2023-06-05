from django.shortcuts import render


def works(request):
    return render(request, "works/works.html")


def works_single(request):
    return render(request, "works/works-single.html")

