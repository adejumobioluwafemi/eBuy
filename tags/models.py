from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # Type of obeject to tag e.g product, video, article
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # ID of such object
    object_id = models.PositiveIntegerField()
    # field to read actual object which particular tag is applied to
    content_object = GenericForeignKey()