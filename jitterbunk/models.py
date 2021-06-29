import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    time = models.DateTimeField('time published of bunk')


    def __str__(self):
        #return ("{} bunked {} at {}").format(self.from_user, self.to_user, self.time)
        return str(self.from_user) + " bunked " + str(self.to_user) + " at this time: " + str(self.time)


  


