from django.shortcuts import render

from proba_strzelnicza.models import Shot


def index(request):
    return render(request, "index.html", {"proba_strzelnicza": Shot.objects.all()})


def shot(request, sample_id):
    shot = Shot.objects.get(sample_id=sample_id)
    return render(request, "proba_strzelnicza.html", {"proba_strzelnicza": shot})
