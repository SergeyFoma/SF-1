from django.shortcuts import render,get_object_or_404
from recipe.models import Category,  Post, Post_recipes, Tag

def index(request):
	#cat=Category.objects.filter(active=True)
	#tags=Tag.objects.filter(active=True)
	context={
		#'cat':cat,
		#'tags':tags,
	}
	return render(request,'recipe/index.html',context)

def categorys(request,cat_slug):
	cats=get_object_or_404(Category,slug=cat_slug)
	#cat=Category.objects.filter(active=True)
	post=Post.objects.filter(categ=cats).order_by('pk')
	context={
		'cats':cats,
		#'cat':cat,
		'post':post,
	}
	return render(request,'recipe/categorys.html',context)



def post_recip(request,pr_slug):
	pr=get_object_or_404(Post,slug=pr_slug)
	post_r=Post_recipes.objects.filter(post=pr).order_by('pk')
	#cat=Category.objects.filter(active=True)
	context={
		'pr':pr,
		'post_r':post_r,
		#'cat':cat,
	}
	return render(request,'recipe/post_recip.html',context)

def tags(request,tag_slug):
	tag=get_object_or_404(Tag,slug=tag_slug)
	posts=Post.objects.filter(tag=tag)
	#tags=Tag.objects.filter(active=True)
	context={
		#'tags':tags,
		'posts':posts,
	}
	return render(request,'recipe/tags.html',context)