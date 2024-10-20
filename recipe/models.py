from django.db import models

class Category(models.Model):
	name=models.CharField(max_length=100,verbose_name='Наименование')
	slug=models.SlugField(unique=True,verbose_name='Слаг')
	active=models.BooleanField(default=True)
	image=models.ImageField(upload_to='media/%Y/%m/%d',verbose_name='Фото')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Категория'
		verbose_name_plural='Категории'

# class Subcategory(models.Model):
# 	name=models.CharField(max_length=100,verbose_name='Наименование')
# 	slug=models.SlugField(unique=True,verbose_name='Слаг')
# 	active=models.BooleanField(default=True)
# 	image=models.ImageField(upload_to='media/%Y/%m/%d',verbose_name='Фото')
# 	categ=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='scat')

# 	def __str__(self):
# 		return self.name

# 	class Meta:
# 		verbose_name='Подкатегория'
# 		verbose_name_plural='Подкатегории'

class Tag(models.Model):
	name=models.CharField(max_length=100)
	active=models.BooleanField(default=False)
	slug=models.SlugField(unique=True,verbose_name='Слаг')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Тег'
		verbose_name_plural='Теги'

class Post(models.Model):
	title=models.CharField(max_length=255,verbose_name='Заглавие')
	text=models.TextField(verbose_name='Текст статьи')
	image=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name="Фото")
	active=models.BooleanField(default=False)
	slug=models.SlugField(unique=True,max_length=50)
	categ=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_post',null=True)
	tag=models.ManyToManyField(Tag,related_name='tag_post')
	date=models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Статья'
		verbose_name_plural='Стaтьи'

class Post_recipes(models.Model):
	title=models.CharField(max_length=255,verbose_name='Заглавие',null=True,blank=True)
	image=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name="Фото",null=True,blank=True)
	text=models.TextField(verbose_name='Текст статьи')
	author=models.CharField(max_length=255,verbose_name='Aвтор статьи',null=True,blank=True)
	slug=models.SlugField(unique=True,max_length=50)
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_recipes')
	url=models.CharField(max_length=255,verbose_name='Url site',null=True,blank=True)

	# def __str__(self):
	# 	return self.title

	class Meta:
		verbose_name='Рецепт'
		verbose_name_plural='Рецепты'