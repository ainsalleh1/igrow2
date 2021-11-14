from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

# Create your models here.


class Feed(models.Model):
    class Meta:
        db_table = 'Feed'
    Title = models.CharField(max_length=255, blank=True)
    Message = models.CharField(max_length=255, blank=True)
    Photo = models.ImageField(upload_to ='images/')
    Video = models.FileField(upload_to='uploads/', null=True)
    Graph = models.FileField(upload_to='uploads/')

    def showvideo(request):

        lastvideo = video.objects.last()
        videofile = lastvideo.videofile
    
        form = SharingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context= {'videofile': videofile, 'form': form}

        return render(request, 'LOGIN/sharing.html', context)
    #def __str__(self):
       # return self.Message + ": " + str(self.videofile)

class Comment(models.Model):
    class Meta:
        db_table = 'Comment'    
    Message = models.CharField(max_length=255)
    Pictures = models.ImageField(upload_to='uploads/')
    Video = models.FileField(upload_to='uploads/')
