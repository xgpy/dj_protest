#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response,render,redirect
from django.template.context_processors import request
from __builtin__ import int
from test.test_pydoc import expected_data_docstrings
import json
from blogs.com_mod.com_mod import str_int
from webapp.models import usertype,user
from com_dbs.models import blogs_chat,python_title

def my_add(request,tablename='',colval1='',colval2='',colval3='',colval4=''):
    tablename.objects.create(username=colval1,password=colval2,email=colval3,user_type=colval4)
#     return '新增成功'
    return '注册成功'
def user_select(request,name):
    usernum=user.objects.filter(username=name).count()
    return usernum
def chat_add(request,username='',chat_cont=''):
    blogs_chat.objects.create(username=username,chat_cont=chat_cont)
    return 1
def my_delete(request,tablename,id):
    tablename.objects.get(id=id).delete()
#     return HttpResponse('ok')
    print request.POST['dat']
    data={'status':1,'msg':'请求成功','data':[11,22,33]}
    return HttpResponse(json.dumps(data))

def my_update(request,tablename,id,hostname):
    obj=tablename.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
    return HttpResponse('ok')

def pytitle_update(request,title):
    obj=python_title.objects.get(title=title)
    visitcount=obj.visit_count+1
    obj.visit_count=visitcount
    obj.save()
    return 1

def com_select(tablename):
    data=tablename.objects.all()
    return data

def pycont_filter(tablename,fieldvalue):
    data=tablename.objects.filter(cont_title=fieldvalue)
    return data
def pytitle_filter(tablename,fieldvalue):
    data=tablename.objects.filter(title=fieldvalue)
    return data
def com_select_filter(tablename,fil):
    data=tablename.objects.filter(t_level=fil)
    return data
def comcon_select_filter(tablename,title1,fil):
    if fil==1:
        data=tablename.objects.filter(t_level=fil,title=title1)
    else:
        data=tablename.objects.filter(t_level=fil)
    return data
def adddata_select(tablename,id):
    data=tablename.objects.get(id=id)
    return data

def my_select(request,cur_page,tablename):
    page_row=str_int(request.COOKIES.get('pager_num',3),3)
    print request.COOKIES.get('pager_num')
    cur_page=str_int(cur_page, 1)
    start_page=(cur_page-1)*page_row
    end_page=cur_page*page_row
    final_res={}
    final_res['cur_page']=cur_page
    total_rows=tablename.objects.all().count()
    res1=divmod(total_rows, page_row)
    if res1[1]:
        nu_pages=res1[0]+1
    else:
        nu_pages=res1[0]
    final_res['page_hlobj']=tablename.objects.all()[start_page:end_page]
    final_res['page_row']=tablename.objects.all()[start_page:end_page].count()
    pre_ps=[]
    if cur_page > 4:
        pre_ps.append('...')
        for p in range(cur_page-3,cur_page):
            pre_ps.append(p)
    else:
        for p in range(1,cur_page):
            pre_ps.append(p)
    final_res['pre_pages']=pre_ps
    end_ps=[]
    if cur_page < nu_pages-3:
        for e in range(cur_page+1,cur_page+4):
            end_ps.append(e)
        end_ps.append('...')
    else:
        for e in range(cur_page+1,nu_pages+1):
            end_ps.append(e)
    final_res['last_pg']=None
    final_res['next_pg']=None
    if cur_page>1:
        final_res['last_pg']=cur_page-1
    if cur_page< nu_pages:
        final_res['next_pg']=cur_page+1
    final_res['end_pages']=end_ps
    final_res['end_pg']=nu_pages
    return final_res



