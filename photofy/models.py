from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your models here.
class Group(models.Model):
    # pass
    groupname = models.CharField(max_length=50,default='NA')

class Photos(models.Model):
    # pass
    groupid = models.ForeignKey(Group,related_name='gname',on_delete=models.CASCADE)
    # photoid = models.IntegerField()
    # owner = models.CharField(max_length=20)
    photourl = models.URLField(max_length=200) #used to sotre url of photo
    title = models.CharField(max_length=200,default='No Title')
    user_owner = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,default=User.objects.get(username='admin'))

class CeleryData(models.Model):
    celeryid = models.CharField(max_length=100)

#a token will be created each time a new user is created
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    #capture the post save signal on User table and crete a token for user
    if created:
        Token.objects.create(user=instance)
        print('creating a user token has been generated')