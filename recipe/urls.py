from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('categorys/<slug:cat_slug>/',views.categorys,name='categorys'),
	#path('post/<slug:post_slug>/',views.post,name='post'),
	path('post_recip/<slug:pr_slug>/',views.post_recip,name='post_recip'),
	path('tags/<slug:tag_slug>/',views.tags,name='tags'),
]
