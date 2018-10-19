from django.db import models
from django.utils import timezone

class Club(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    host = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=100)
    stylesheet = models.CharField(max_length=100)
    instagram_href = models.URLField()
    instagram_text = models.CharField(max_length=100)
    facebook_href = models.URLField()
    facebook_text = models.CharField(max_length=100)
    twitter_href = models.URLField()
    twitter_text = models.CharField(max_length=100)
    google_href = models.URLField()
    google_text = models.CharField(max_length=100)
    youtube_href = models.URLField()
    youtube_text = models.CharField(max_length=100)
    sendmail_href = models.EmailField()
    sendmail_text = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['host']),
        ]

class News(models.Model):
    club = models.ForeignKey('Club', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    summary	= models.CharField(max_length=200)
    text = models.TextField()
    image = models.CharField(max_length=100, blank=True, null=True)
    preferential = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    date_creation = models.DateTimeField(default=timezone.now)
    date_publication = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date_publication = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#    class Meta:
#        indexes = [
#            models.Index(fields=['club', 'date_publication']),
#        ]

class Sponsor(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    href = models.URLField()

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
