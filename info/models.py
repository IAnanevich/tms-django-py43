from django.db import models


class InfoBlog(models.Model):
    """"""

    name = models.CharField(max_length=30, null=False)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)
    is_deleted = models.BooleanField(null=False, default=False)
