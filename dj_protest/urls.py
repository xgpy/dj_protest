"""dj_protest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webapp import views
from com_mod import login
from blogs import views as blogviews
from blogs.com_mod.mod_adddata import addblogs,updateblogs
from hcharts import views as hchartsviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^identf_code/', views.identf_code),
    url(r'^logout/', login.mlogout),
    url(r'^agent_api/', views.agent_api),
    url(r'^blogs/$', blogviews.blogs),
    url(r'^visitnum/$', blogviews.visitnum),
    url(r'^blogs/(\S*)/$', blogviews.blogs_obj),
    url(r'^curblogs/$', blogviews.curblogs),
    url(r'^adddata/', blogviews.adddata),
    url(r'^sorry/', blogviews.sorryservice),
    url(r'^blogs_cont/', blogviews.blog_cont_ajax),
    url(r'^web_addchat/', blogviews.webchat_adddata),
    url(r'^webchat_incre/', blogviews.webchat_increment),
    url(r'^commentpy/', blogviews.comment_py),
    url(r'^replysubmit/', blogviews.reply_submit),
    url(r'^addblogs/', addblogs),
    url(r'^updateblogs/', updateblogs),
    url(r'^hcharts/', hchartsviews.hcharts),
    url(r'^hchartsdata/', hchartsviews.hchartsdata),
]
