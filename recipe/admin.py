from django.contrib import admin
from recipe.models import Category,Tag, Post, Post_recipes

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','name','slug','active','image']
	prepopulated_fields={'slug':['name',]}

# @admin.register(Subcategory)
# class SubcategoryAdmin(admin.ModelAdmin):
# 	list_display=['id','name','slug','active','image','categ']
# 	prepopulated_fields={'slug':['name',]}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display=['id','name','active','slug']
	prepopulated_fields={'slug':['name',]}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display=['id','title','text','image','active','slug','categ','date']
	prepopulated_fields={'slug':['title',]}

@admin.register(Post_recipes)
class Post_recipesAdmin(admin.ModelAdmin):
	list_display=['id','title','image','text','author','slug','post','url']
	prepopulated_fields={'slug':['title',]}
