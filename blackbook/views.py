from django.http import HttpResponse, Http404
from django.template import Context, loader

from blackbook.models import Category, Picture

def index(request):
    categories = Category.objects.all()
    template = loader.get_template('blackbook/index.html')
    context = Context({'object_list': categories})
    return HttpResponse(template.render(context))

def detail(render, slug):
	try:
		picture = Picture.objects.get(slug=slug)
	except Picture.DoesNotExist:
		raise Http404
	template = loader.get_template('blackbook/detail.html')
	context = Context({'object': picture})
	return HttpResponse(template.render(context))

def show_category(render, slug):
    try:
        pictures = Picture.objects.filter(category__slug__exact=slug)
    except Picture.DoesNotExist:
        raise Http404
    template = loader.get_template('blackbook/show-category.html')
    context = Context({'object_list': pictures})
    return HttpResponse(template.render(context))
