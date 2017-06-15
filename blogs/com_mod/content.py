#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.template.context_processors import request
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,redirect
import json
from django.template.context import RequestContext
from blogs.com_mod.formtable import auser
from blogs.com_mod.com_mod import str_int
from blogs.com_mod.cdus_my import my_add,my_select,adddata_select,pytitle_filter
from blogs.com_mod.cdus_my import comcon_select_filter,pycont_filter,com_select_filter
from blogs.com_mod.cdus_my import com_select
from webapp.models import usertype
from com_dbs.models import python_cont,python_stru,python_title
from com_dbs.models import blogs_chat


def python_blogs(request):
    py_dic={}
    d1={}
    py_title_1=com_select_filter(python_title,1)
    py_title_2=com_select_filter(python_title,2)
    py_title_3=com_select_filter(python_title,3)
    d1[1]=py_title_1[0]
    d1['data']=[]
    d=[]
    py_dic=[]
    for p2 in py_title_2:
        d2={}
        d3={}
        d3[3]=0
        d2['data']=[]
        d3['data']=[]
        for p3 in py_title_3:
            if p2.title==p3.pre_title:
                d3['data'].append(p3)
        d2[2]=p2
        d2['data'].append(d3)
        d1['data'].append(d2)
    py_dic.append(d1)
    return py_dic

def comcon_blogs(request):
    py_dic={}
    d1={}
    title1=request.session['cur_stru_title']
    py_title_1=comcon_select_filter(python_title,title1,1)
    py_title_2=comcon_select_filter(python_title,title1,2)
    py_title_3=comcon_select_filter(python_title,title1,3)
    d1[1]=py_title_1[0]
    d1['data']=[]
    d=[]
    py_dic=[]
    for p2 in py_title_2:
        d2={}
        d3={}
        d2['data']=[]
        d3['data']=[]
        if p2.pre_title==py_title_1[0].title:
            d3[3]=0
            for p3 in py_title_3:
                if p2.title==p3.pre_title:
                    d3['data'].append(p3)
            d2[2]=p2
            d2['data'].append(d3)
            d1['data'].append(d2)
    py_dic.append(d1)
    return py_dic

def python_content(request):
    fieldvalue=request.session.get('cur_stru_title')
    py_cont=pycont_filter(python_cont,fieldvalue)
    return py_cont

def python_tit(request):
    fieldvalue=request.session.get('cur_stru_title')
    py_title=pytitle_filter(python_title,fieldvalue)
    return py_title

def chat_select(request):
    chatnum=blogs_chat.objects.all().count()
    if chatnum!=0:
        if chatnum<6:
            chat_d=list(reversed(blogs_chat.objects.order_by('-chat_date')))
            request.session['chat_lastid']=chat_d[chatnum-1].id
        else:
            chat_d=list(reversed(blogs_chat.objects.order_by('-chat_date')[:6]))
            request.session['chat_lastid']=chat_d[5].id
        return chat_d
    else:
        return

def blog_pyadd(request,title='',level='',pre_title='',content=''):
    python_title.objects.create(title=title,t_level=level,pre_title=pre_title)
    python_cont.objects.create(cont_title=title,cont_py=content)
    return '提交成功！！！'

def blog_pyupdate(request,title='',level='',pre_title='',content=''):
    print content
    obj=python_cont.objects.get(cont_title=title)
    obj.cont_py=content
    obj.save()
    return '更新成功！！！'



