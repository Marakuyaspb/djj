from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
#from taggit.models import Tag


def blog(request, tag_slug=None):
	posts = Post.published.all()
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		blog = blog.filter(tags__in=[tag])

	paginator = Paginator(posts, 1)
	page_number = request.GET.get('page', 1)
	posts = paginator.page(page_number)

	return render(request,
		'blog/blog.html',
		{'posts': posts, 
		'tag': tag})


def single_blog_post(request, id):
	try:
		post = Post.objects.get(id = id)
	except:
		raise Http404('Такого текста о диванах пока нет :(')
	return render(request,'blog/single_blog_post.html', {'single_blog_post': post})

