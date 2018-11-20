from django.contrib import admin
from .models import *
#from .models import Club,Sponsor,ContactMessage,News,Gallery,GalleryObject,Season,Age

class SocialAdmin(admin.ModelAdmin):
    list_display = ('name','href','icon')

admin.site.register(Social, SocialAdmin)

class AgeAdmin(admin.ModelAdmin):
    list_display = ('name','start_years', 'end_years')

admin.site.register(Age, AgeAdmin)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name','start_date', 'end_date')

admin.site.register(Season, SeasonAdmin)

class ClubSocialInline(admin.TabularInline):
    model = ClubSocial
    extra = 6
class SponsorInline(admin.TabularInline):
    model = Sponsor
    extra = 10

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
    inlines = [ClubSocialInline, SponsorInline]

admin.site.register(Club, ClubAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('club','title', 'image', 'href')

admin.site.register(Sponsor, SponsorAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('club','request_date', 'response_date', 'phone', 'email', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('club','title','summary','preferential','date_creation','date_publication')

admin.site.register(News, NewsAdmin)

class GalleryObjectInline(admin.TabularInline):
    model = GalleryObject
    extra = 10

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('club','date', 'title','gallery_type')
    inlines = [GalleryObjectInline]

admin.site.register(Gallery, GalleryAdmin)

class PeopleSocialInline(admin.TabularInline):
    model = PeopleSocial
    extra = 3

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('nick','name', 'surname','birth_date')
    inlines = [PeopleSocialInline]

admin.site.register(People, PeopleAdmin)

