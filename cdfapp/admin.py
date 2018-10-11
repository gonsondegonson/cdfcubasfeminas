from django.contrib import admin
from .models import Club,Sponsor,ContactMessage

# RegSponsorr your models here.
class ClubAdmin(admin.ModelAdmin):
#    fields = ['name', 'title']
    list_display = ('name', 'title')
    fieldsets = [
        (None,      {'fields': ['name', 'title']}),
        ('Estilo',  {'fields': ['image', 'stylesheet']}),
        ('Correo',  {'fields': ['sendmail_href', 'sendmail_text']}),
        ('Redes',   {'fields': ['instagram_href', 'instagram_text',
                                'facebook_href', 'facebook_text',
                                'twitter_href', 'twitter_text',
                                'google_href', 'google_text',
                                'youtube_href', 'youtube_text']}),
    ]

admin.site.register(Club, ClubAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'href')

admin.site.register(Sponsor, SponsorAdmin)

class SponsorContactMessage(admin.ModelAdmin):
    list_display = ('request_date', 'response_date', 'phone', 'email', 'message')

admin.site.register(ContactMessage, SponsorContactMessage)
