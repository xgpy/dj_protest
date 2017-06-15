#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.template.context_processors import request
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,redirect
import json,md5
from django.template.context import RequestContext
from blogs.com_mod.formtable import auser
from blogs.com_mod.com_mod import str_int
from blogs.com_mod.cdus_my import my_add,my_select,adddata_select,user_select
from webapp.models import usertype
from blogs.com_mod.content import blog_pyadd,blog_pyupdate

def madddata(request,tablename,filehtml):
    res={'data':None,'error':''}
    res['data']=auser()
#     print request.session.get('login',False)
#     print request.session['login']
#     if request.session.get('login',False):
    if request.method=='POST':
        checkform=auser(request.POST)
        checkresult=checkform.is_valid()
        if checkresult:
            chk_usernm=checkform['username'].value()
            chk_passwd=checkform['password'].value()
            m=md5.md5(chk_passwd)
            chk_passwd=m.hexdigest()
            chk_email=checkform['email'].value()
            chk_userty=checkform['user_type'].value()
            chk_userty=adddata_select(usertype, chk_userty)
            usernum=user_select(request, chk_usernm)
            if usernum==0:
                my_res=my_add(request, tablename=tablename, colval1=chk_usernm, colval2=chk_passwd, colval3=chk_email,colval4=chk_userty)
                res['msg']=my_res
            else:
                res['msg']='用户名已存在！！！'
        else:
            firerrmsg=checkform.errors.as_data().values()[0][0].message
            res['msg']=firerrmsg
            res['data']=checkform
    response_r = render_to_response(filehtml,res)
    return response_r
#     else:
#         return redirect('/login/')

# def mdeldata(request):
#     if request.method=='POST':
# #         delrequire=request.POST.data
#         hostid=request.POST['dat']
#         if hostid:
#             return my_delete(request, host, hostid)
#         else:
#             data={'status':0,'msg':'ID can not NULL','data':[11,22,33]}
#             return HttpResponse(json.dumps(data))
        

def addblogs(request):
    res={}
    if request.session.get('curuser','admin')=='guan':
        if request.method=='POST':
            title=request.POST['blogtitle']
            level=request.POST['bloglevel']
            pretitle=request.POST['pretitle']
            content=request.POST['blogcontent']
            res['msg']=blog_pyadd(request, title=title, level=level, pre_title=pretitle, content=content)
            res['title']=title
            return render_to_response('blogs/addblogs_data.html',res)
        else:
            return render_to_response('blogs/addblogs_data.html')
    else:
        return HttpResponse('抱歉，您没有该权限！！！')
    
def updateblogs(request):
    res={}
    if request.session.get('curuser','admin')=='guan':
        if request.method=='POST':
            title=request.POST['blogtitle']
            level=request.POST['bloglevel']
            pretitle=request.POST['pretitle']
            content=request.POST['blogcontent']
            res['msg']=blog_pyupdate(request, title=title, level=level, pre_title=pretitle, content=content)
            res['title']=title
            return render_to_response('blogs/updateblogs_data.html',res)
        else:
            return render_to_response('blogs/updateblogs_data.html')
    else:
        return HttpResponse('抱歉，您没有该权限！！！')






