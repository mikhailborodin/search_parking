from __future__ import unicode_literals

from django.contrib.gis.db import models

STATUS = (
    ('No car parking', 'No car parking'),
    ('Service unavailable', 'Service unavailable'),
)


class Parking(models.Model):
    title = models.CharField(max_length=255)
    geometry = models.MultiPolygonField()
    is_free = models.BooleanField(default=True)
    status = models.CharField(max_length=255, choices=STATUS)

    def __unicode__(self):
        return self.title
