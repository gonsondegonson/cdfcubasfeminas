from django.shortcuts import render
from django.core.paginator import Paginator

from .functions import GetParameter, GetRequestId, GetObjectId
from .forms import ContactForm
from .models import  Social, Club, Season, Cover, News, Team, TeamMember, Gallery, PeopleSocial, PeoplePhoto, Installation, InstallationImage, TeamInstallation, ClubEquipement

def google(request):

    return render(request, 'google116a2281a3dd79be.html')

def home(request):
    club = Club.objects.get(host=request.get_host())
    covers = Cover.objects.filter(club=club.id, active=True)
    news = News.objects.filter(club=club.id, date_publication__isnull=False, featured=True)

    id = GetRequestId(request)
    current = GetObjectId(id, news)

    return render(request, 'home.html',  {'club': club, 'covers': covers, 'news': news, 'current': current})

def news(request):
    club = Club.objects.get(host=request.get_host())
    news = News.objects.filter(club=club.id).order_by('-date_publication').filter(date_publication__isnull=False)

    id = GetRequestId(request)
    current = GetObjectId(id, news)

    page = request.GET.get('page', 1)
    paginator = Paginator(news, 10)
    news_page = paginator.get_page(page)

    return render(request, 'news.html',  {'club': club, 'news': news_page, 'current': current})

def installations(request):
    club = Club.objects.get(host=request.get_host())

    id = GetParameter(request, 'Id')
    if id == None:
        teamId = GetParameter(request, 'Team')
        if teamId == None:
            installations = Installation.objects.filter(club=club.id)
            return render(request, 'installations.html',  {'club': club, 'installations': installations})
        else:
            team = Team.objects.get(id=int(teamId))
            teaminstallations = TeamInstallation.objects.filter(team_id=int(teamId))
            return render(request, 'teaminstallations.html',  {'club': club, 'team': team, 'teaminstallations': teaminstallations})
    else:
        installation = Installation.objects.get(id=int(id))
        installationimages = InstallationImage.objects.filter(installation_id=int(id))
        teamsinstallation = TeamInstallation.objects.filter(installation_id=int(id))
        return render(request, 'installation.html',  {'club': club, 'installation': installation, 'installationimages': installationimages, 'teamsinstallation': teamsinstallation})

def equipement(request):
    club = Club.objects.get(host=request.get_host())
    equipements = ClubEquipement.objects.filter(club=club.id, season=Season.current().id)

    return render(request, 'equipement.html',  {'club': club, 'equipements': equipements})

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
    socials= Social.objects.all()

    id = GetRequestId(request)
    teammember = TeamMember.objects.get(id=id)
    teammemberhistorics = TeamMember.objects.filter(people=teammember.people.id)

    peoplesocials = PeopleSocial.objects.filter(people=teammember.people.id)
    for social in socials:
        social.href = None
        for peoplesocial in peoplesocials:
            if peoplesocial.social.id == social.id:
                social.href = peoplesocial.href

    peoplephotos = PeoplePhoto.objects.filter(people=teammember.people.id)

    return render(request, 'member.html',  {'club': club, 'teammember': teammember, 'socials': socials, 'teammemberhistorics': teammemberhistorics, 'peoplephotos': peoplephotos})

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

    active = GetParameter(request, 'Active')
    if active == None:
        galleries = Gallery.objects.filter(club=club.id, gallery_type='PH', active=True).order_by('-date')
    else:
        if active.upper() == 'FALSE':
            galleries = Gallery.objects.filter(club=club.id, gallery_type='PH', active=False).order_by('-date')
        else:
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
