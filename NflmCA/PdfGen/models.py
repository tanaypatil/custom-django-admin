from django.db import models


class Images(models.Model):
    img = models.ImageField()
    alt_text = models.CharField(max_length=10)

    def __str__(self):
        return self.alt_text

    def __unicode__(self):
        return self.alt_text
