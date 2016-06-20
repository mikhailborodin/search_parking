from tastypie.contrib.gis.resources import ModelResource
from models import Parking
from django.contrib.gis import geos
from django.http import Http404


class ParkingResource(ModelResource):
    class Meta:
        queryset = Parking.objects.all()

    def obj_get_list(self, bundle, **kwargs):
        lat = float(bundle.request.GET['latitude'])
        lon = float(bundle.request.GET['longitude'])
        center = geos.Point((lon, lat), srid=4326)
        dd = (float(bundle.request.GET['distance']) / 40000) * 360
        objects = Parking.objects.filter(geometry__dwithin=(center, dd))
        if objects:
            return objects
        else:
            raise Http404('parking not found in radius: %s km' % bundle.request.GET['distance'])

    def dehydrate(self, bundle):
        bundle.data['type'] = "Feature"
        return bundle