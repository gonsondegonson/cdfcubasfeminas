from django.contrib import admin
from .models import Club,Sponsor,ContactMessage,News

class ClubAdmin(admin.ModelAdmin):
#    fields = ['name', 'title']
    list_display = ('host','name', 'title')
    fieldsets = [
        (None,      {'fields': ['name', 'title','host']}),
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
    list_display = ('club','title', 'image', 'href')

admin.site.register(Sponsor, SponsorAdmin)

class SponsorContactMessage(admin.ModelAdmin):
    list_display = ('club','request_date', 'response_date', 'phone', 'email', 'message')

admin.site.register(ContactMessage, SponsorContactMessage)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('club','title','summary','preferential','date_creation','date_publication')

admin.site.register(News, NewsAdmin)

