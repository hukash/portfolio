from django.http import HttpResponse, Http404
from django.template import Context, loader

from blackbook.models import Category, Photo, Video

def index(request):
    categories = Category.objects.all()
    template = loader.get_template('blackbook/index.html')
    context = Context({'object_list': categories})
    return HttpResponse(template.render(context))

def detail(render, slug):
	try:
		photo = Photo.objects.get(slug=slug)
	except Photo.DoesNotExist:
		raise Http404
	template = loader.get_template('blackbook/detail.html')
	context = Context({'object': photo})
	return HttpResponse(template.render(context))

def show_category(render, slug):
    photos = Photo.objects.filter(
                category__slug__exact=slug
             ).filter(
                active=True
             )
    try:
        category = Category.objects.get(slug=slug)
        categories = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404
    template = loader.get_template('blackbook/show-category.html')
    context = Context({'object_list': photos, 'category': category, 'categories': categories})
    return HttpResponse(template.render(context))

def show_video(render, slug):
    try:
        video = Video.objects.get(slug=slug)
        # add youtube id resolver
        splitted_url = video.url.split('/')
        url_id = splitted_url[-1]
    except Video.DoesNotExist:
        raise Http404
    template = loader.get_template('blackbook/video.html')
    context = Context({'object': video, 'url_id': url_id})
    return HttpResponse(template.render(context))
