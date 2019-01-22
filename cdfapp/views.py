from django.shortcuts import render
from django.core.paginator import Paginator

from .functions import GetParameter, GetRequestId, GetObjectId
from .forms import ContactForm
from .models import  Season, Club, Cover, News, Team, TeamMember, Gallery, Rol

def home(request):
    season = Season.current()
    club = Club.objects.get(host=request.get_host())
    covers = Cover.objects.filter(club=club.id, active=True)
    news = News.objects.filter(club=club.id, date_publication__isnull=False, featured=True)

    id = GetRequestId(request)
    current = GetObjectId(id, news)

    return render(request, 'home.html',  {'season': season, 'club': club, 'covers': covers, 'news': news, 'current': current})

def news(request):
    club = Club.objects.get(host=request.get_host())
    news = News.objects.filter(club=club.id).order_by('-date_publication').filter(date_publication__isnull=False)

    id = GetRequestId(request)
    current = GetObjectId(id, news)

    page = request.GET.get('page', 1)
    paginator = Paginator(news, 10)
    news_page = paginator.get_page(page)

    return render(request, 'news.html',  {'club': club, 'news': news_page, 'current': current})

def team(request):
    teamId = int(GetParameter(request, 'Id'))

    club = Club.objects.get(host=request.get_host())
    team = Team.objects.get(id=teamId)

    return render(request, 'team.html',  {'club': club, 'team': team})

def members(request):
    teamId = int(GetParameter(request, 'Id'))

    club = Club.objects.get(host=request.get_host())
    team = Team.objects.get(id=teamId)
    teammembers = TeamMember.objects.filter(team=teamId).order_by('number')

    return render(request, 'members.html',  {'club': club, 'team': team, 'teammembers': teammembers})

def member(request):
    club = Club.objects.get(host=request.get_host())

    id = GetRequestId(request)

    return render(request, 'member.html',  {'club': club})

def contact(request):
    club = Club.objects.get(host=request.get_host())

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contactmessage = form.save(commit=False)
            contactmessage.club = club
            contactmessage.save()
            return render(request, 'contactmessage_ok.html',  {'club': club, 'item': contactmessage})
    else:
        form = ContactForm()

    return render(request, 'contactmessage.html', {'form': form, 'club': club})

def photogallery(request):
    club = Club.objects.get(host=request.get_host())
    galleries = Gallery.objects.filter(club=club.id, gallery_type='PH').order_by('-date')

    id = GetRequestId(request)
    current = GetObjectId(id, galleries)

    page = request.GET.get('page', 1)
    paginator = Paginator(galleries, 10)

    gallery_page = paginator.get_page(page)

    return render(request, 'photogallery.html',  {'club': club, 'galleries': gallery_page, 'current': current})

def videogallery(request):
    club = Club.objects.get(host=request.get_host())
    galleries = Gallery.objects.filter(club=club.id, gallery_type='VD').order_by('-date')

    id = GetRequestId(request)
    current = GetObjectId(id, galleries)

    page = request.GET.get('page', 1)
    paginator = Paginator(galleries, 10)

    gallery_page = paginator.get_page(page)

    return render(request, 'videogallery.html',  {'club': club, 'galleries': gallery_page, 'current': current})
#    return render(request, 'test.html',  {'club': club, 'galleries': gallery_page, 'current': current})

#    raise Exception('Objeto' + str(current.id))
