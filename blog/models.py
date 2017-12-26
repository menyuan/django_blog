# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
# Create your models here.
#用户模型
#采用继承方式扩展用户信息

class User(models.Model):
	username=models.CharField(max_length=50,unique=True,verbose_name='用户名')
	password=models.CharField(max_length=100,verbose_name='密码')
	avatar=models.ImageField(upload_to='avatar/%Y/%m',default='avatar/default.png',max_length=255)
	qq=models.CharField(max_length=20,blank=True,null=True,verbose_name='QQ号码')
	mobile=models.CharField(max_length=11,blank=True,null=True,unique=True,verbose_name='手机号码')

	class Meta:
		verbose_name='用户'
		verbose_name_plural=verbose_name
		ordering=['-id']

	def __unicode__(self):
		return self.username


class Tag(models.Model):
	name=models.CharField(max_length=30,verbose_name='标签名称')

	class Meta:
		verbose_name='标签'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=30,verbose_name='分类名称')
	index=models.IntegerField(default=999,verbose_name='分类的排序')

	class Meta:
		verbose_name='分类'
		verbose_name_plural=verbose_name

	def __unicode__(self):
		return self.name

#自定义Manager类
class ArticleManager(models.Manager):
	def distinct_date(self):
		distinct_date_list=[]
		date_list=self.values('date_publish')
		for date in date_list:
			date=date['date_publish'].strftime('%Y/%m文档存档')
			if date not in distinct_date_list:
				distinct_date_list.append(date)
		return distinct_date_list

#文章模型
class Article(models.Model):
	title=models.CharField(max_length=50,verbose_name='文章标题')
	desc=models.CharField(max_length=50,verbose_name='文章描述')
	content=UEditorField('文章内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
	click_count=models.IntegerField(default=0,verbose_name='点击次数')
	is_recommend=models.IntegerField(default=0,verbose_name='浏览次数')
	date_publish=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
	user=models.ForeignKey(User,verbose_name='用户')
	Category=models.ForeignKey(Category,blank=True,verbose_name='分类')
	tag=models.ManyToManyField(Tag,verbose_name='标签')

	objects=ArticleManager.distinct_date()

	def get_absolute_url(self):
		return reverse('article_detail',args=(self.id,))

	class Meta:
		verbose_name='文章'
		verbose_name_plural=verbose_name
		ordering=['-date_publish']

	def __unicode__(self):
		return self.title

#评论模型
class Comment(models.Model):
	content=models.TextField(verbose_name='评论内容')
	date_publish=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
	user=models.ForeignKey(User,blank=True,null=True,verbose_name='用户')
	article=models.ForeignKey(Article,blank=True,null=True,verbose_name='文章')
	pid=models.ForeignKey('self',blank=True,null=True,verbose_name='父级评论')

	class Meta:
		verbose_name='评论'
		verbose_name_plural=verbose_name
		ordering=['-date_publish']

	def __unicode__(self):
		return str(self.id)

#友情链接
class Link(models.Model):
	title=models.CharField(max_length=50,verbose_name='标题')
	description=models.CharField(max_length=200,verbose_name='友情链接描述')
	callback_url=models.URLField(verbose_name='url地址')
	date_publish=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
	index=models.IntegerField(default=999,verbose_name='从小到大排序')

	class Meta:
		verbose_name='友情链接'
		verbose_name_plural=verbose_name
		ordering=['index','id']

	def __unicode__(self):
		return self.title