import random
import operator
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def current():
        current_date = timezone.now()
        seasons = Season.objects.filter(start_date__lte=current_date,end_date__gte=current_date)
        for season in seasons:
            return season

    def __str__(self):
        return self.name

class Age(models.Model):
    name = models.CharField(max_length=100)
    start_years = models.IntegerField()
    end_years = models.IntegerField()

    def current(birth_date):
        season = Season.current()
        years = season.start_date.year - birth_date.year
        ages = Age.objects.filter(start_years__lte=years,end_years__gte=years)
        for age in ages:
            return age

    def __str__(self):
        return self.name

class People(models.Model):
    nick = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateTimeField(blank=True, null=True)

    def social(self):
        return PeopleSocial.objects.filter(people=self.id)

    def __str__(self):
        return self.name + ' ' + self.surname

class PeopleSocial(models.Model):
    people = models.ForeignKey('People', on_delete=models.PROTECT)
    social = models.ForeignKey('Social', on_delete=models.PROTECT)
    href = models.CharField(max_length=100)

    def __str__(self):
        return self.href

class Club(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    host = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)
    stylesheet = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def sponsors(self):
        return Sponsor.index_list(self.id)

    def social(self):
        return ClubSocial.objects.filter(club=self.id).select_related('social')

    class Meta:
        indexes = [
            models.Index(fields=['host']),
        ]

class ClubSocial(models.Model):
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    social = models.ForeignKey('Social', on_delete=models.PROTECT)
    href = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.href

class Cover(models.Model):
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    image = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    href = models.CharField(max_length=100, blank=True, null=True)
    news = models.ForeignKey('News', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return ''

    class Meta:
        indexes = [
            models.Index(fields=['club', 'active']),
        ]

class News(models.Model):
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    summary	= models.CharField(max_length=200)
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    featured = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def html_text(self):
        return format_html(self.text)

    class Meta:
        indexes = [
            models.Index(fields=['club', '-date_publication']),
        ]

class Sponsor(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    href = models.URLField()
    index = models.IntegerField(blank=True, null=True)

    def index_list(id):
        current_date = timezone.now()
        sponsors = Sponsor.objects.filter(club=id,start_date__lte=current_date,end_date__gte=current_date)
        for sponsor in sponsors:
            sponsor.index = random.randint(0, 1000)
        return sorted(sponsors, key=operator.attrgetter('index'))

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    message = models.TextField()
    request_date = models.DateTimeField(default=timezone.now)
    response_date = models.DateTimeField(blank=True, null=True)

    def answered(self):
        self.response_date = timezone.now()
        self.save()

    def __str__(self):
        return self.message

class Gallery(models.Model):
    PHOTO = 'PH'
    VIDEO = 'VD'
    GALLERY_TYPE = (
        (PHOTO, 'Foto'),
        (VIDEO, 'Vídeo'),
    )

    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)
    gallery_type = models.CharField(max_length=2, choices=GALLERY_TYPE, default=PHOTO,)
    image = models.CharField(max_length=100, blank=True, null=True)
    href = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def galleryobjects(self):
        return GalleryObject.objects.filter(gallery=self.id)

    class Meta:
        indexes = [
            models.Index(fields=['club', 'gallery_type', '-date']),
        ]

class GalleryObject(models.Model):
    gallery = models.ForeignKey('Gallery', on_delete=models.PROTECT)
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=100)
    href = models.CharField(max_length=100)

    def __str__(self):
        return self.image

class Team(models.Model):
    season = models.ForeignKey('Season', on_delete=models.PROTECT)
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    age = models.ForeignKey('Age', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Social(models.Model):
    name = models.CharField(max_length=100)
    href = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
