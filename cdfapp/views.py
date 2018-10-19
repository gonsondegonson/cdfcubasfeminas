from django.shortcuts import render
from django.core.paginator import Paginator
#from django.http import HttpResponse
#from django.template.loader import render_to_string
from .forms import ContactForm
from .models import Club, Sponsor, News

def home(request):
    club = Club.objects.get(host=request.get_host())
    sponsors = Sponsor.objects.filter(club=club.id)
    news = News.objects.filter(club=club.id).filter(date_publication__isnull=False)

    paginator = Paginator(news, 2)

    page = request.GET.get('page')
    newslist = paginator.get_page(page)

    return render(request, 'home.html',  {'club': club, 'sponsors': sponsors, 'news': newslist})


def noticias(request):
    club = Club.objects.get(host=request.get_host())
    sponsors = Sponsor.objects.filter(club=club.id)
    news = News.objects.filter(club=club.id)

    paginator = Paginator(news, 2)

    page = request.GET.get('page')
    newslist = paginator.get_page(page)

    return render(request, 'news.html',  {'club': club, 'sponsors': sponsors, 'news': newslist})


def contacto(request):
    club = Club.objects.get(host=request.get_host())
    sponsors = Sponsor.objects.filter(club=club.id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contactmessage = form.save(commit=False)
            contactmessage.club = club
            contactmessage.save()
            return render(request, 'contactmessage_ok.html',  {'club': club, 'sponsors': sponsors, 'item': contactmessage})
#            return HttpResponse(render_to_string('contactmessage_ok.html', {'club': club, 'sponsors': sponsors, 'item': contactmessage}))
    else:
        form = ContactForm()

    return render(request, 'contactmessage.html', {'form': form, 'club': club, 'sponsors': sponsors})
