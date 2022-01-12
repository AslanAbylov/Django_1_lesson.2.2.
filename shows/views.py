from django.shortcuts import render, get_object_or_404
from . import models



def show_all(request):
    shows = models.TVShow.objekts.all()
    return render(request, 'shows_list.html', {'shows': shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TVShow, id=id)
    return render(request, 'shows_detail.html', {'show': show})