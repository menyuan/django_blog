# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def global_setting(request):
	return {'SITE_NAME':settings.SITE_NAME,
			'SITE_DESC':settings.SITE_DESC,
	}
def index(request):
	tags=Tag.objects.all();
	links=Link.objects.all();
	articles=Article.objects.all();
	paginator=Paginator(articles,1)
	page=request.GET.get('page')
	try:
		arts=paginator.page(page)
	except PageNotAnInteger:
		arts=paginator.page(1)
	except EmptyPage:
		arts=paginator.page(paginator.num_pages)
	dates=Article.objects.datetimes('date_publish','month',order="DESC")
	recommend=Article.objects.order_by('is_recommend')
	return render(request,'index.html' ,{'tags':tags,'links':links,'arts':arts,"dates":dates,"recommend":recommend})

def article_detail(request,art_id):
	id=art_id
	article=Article.objects.filter(id=art_id)[0]
	return render(request,'article.html',{'article':article})

