from django.shortcuts import render
from .models import Video
# Pagination for lazy loading
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import VideoFilter

# index page get api
#
# @params [int] page for page number
# @except if page none, default_page = 1
# @except if page > num_pages i.e EmptyPage exception default  becomes num_pages
#
# @return index.html and response data for frontend
def index(request):
    if request.method == "GET":
        page = request.GET.get('page')
        all_videos = Video.objects.all()
        results_per_page = 6
        paginator = Paginator(all_videos, results_per_page)
        try:
            current_page = page
            videos = paginator.page(page)
        except PageNotAnInteger:
            current_page = 1
            videos = paginator.page(1)
        except EmptyPage:
            current_page = paginator.num_pages
            videos = paginator.page(paginator.num_pages)

        response = {
            'videos': videos,
            'has_next': videos.has_next(),
            'next_page': int(current_page) + 1,
            'has_previous': videos.has_previous(),
            'prev_page': int(current_page) - 1
        }
        return render(request, 'Fampay/index.html', response)
