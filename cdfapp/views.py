from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import Club, Sponsor, ContactMessage

#global Club = 1

# Create your views here.
def home(request):
    club = Club.objects.get(id=1)
    sponsors = Sponsor.objects.filter(club=club.id)

    return render(request, 'home.html',  {'club': club, 'sponsors': sponsors})

def contacto(request):

    club = Club.objects.get(id=1)
    sponsors = Sponsor.objects.filter(club=club.id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage = form.save(commit=False)
            ContactMessage.club = club
            ContactMessage.save()
#            return redirect('/')
            return HttpResponse(render_to_string('contactmessage_ok.html', {'club': club, 'sponsors': sponsors, 'item': ContactMessage}))
    else:
        form = ContactForm()

    return render(request, 'contactmessage.html', {'form': form, 'club': club, 'sponsors': sponsors})
