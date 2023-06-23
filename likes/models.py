from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # type of object liked
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID of such object
    object_id = models.PositiveIntegerField()
    # field to read actual user which particular liked an object
    content_object = GenericForeignKey()
