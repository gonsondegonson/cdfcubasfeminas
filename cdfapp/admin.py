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
    extra = 1
class SponsorInline(admin.TabularInline):
    model = Sponsor
    extra = 1

class ClubAdmin(admin.ModelAdmin):
#    fields = ['name', 'title']
    list_display = ('host','name', 'title')
    fieldsets = [
        (None,      {'fields': ['name', 'title','host']}),
        ('Estilo',  {'fields': ['image', 'stylesheet']}),
    ]
    inlines = [ClubSocialInline, SponsorInline]

admin.site.register(Club, ClubAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('club','title', 'image', 'href')

admin.site.register(Sponsor, SponsorAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('club','request_date', 'response_date', 'phone', 'email', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)

class CoverAdmin(admin.ModelAdmin):
    list_display = ('club','image','active','href','news')

admin.site.register(Cover, CoverAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('club','title','summary','date_creation','date_publication')

admin.site.register(News, NewsAdmin)

class GalleryObjectInline(admin.TabularInline):
    model = GalleryObject
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('club','date', 'title','gallery_type')
    inlines = [GalleryObjectInline]

admin.site.register(Gallery, GalleryAdmin)

class PeopleSocialInline(admin.TabularInline):
    model = PeopleSocial
    extra = 1

class PeoplePhotoInline(admin.TabularInline):
    model = PeoplePhoto
    extra = 1

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','birth_date')
    inlines = [PeopleSocialInline, PeoplePhotoInline]

admin.site.register(People, PeopleAdmin)

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1

class TeamAdmin(admin.ModelAdmin):
    list_display = ('season','club', 'age','name')
    inlines = [TeamMemberInline]

admin.site.register(Team, TeamAdmin)

class RolAdmin(admin.ModelAdmin):
    list_display = ('name','rol_type')

admin.site.register(Rol, RolAdmin)

