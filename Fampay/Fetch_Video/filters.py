import django_filters
from .models import Video

class VideoFilter(django_filters.FilterSet):

    class Meta:
        model = Video
        fields = {'title','description','publishedAt'}
