#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from webapp.models import user
from blogs.com_mod.mod_adddata import madddata 
from blogs.com_mod.content import python_blogs,python_content,python_tit
from blogs.com_mod.content import chat_select,comcon_blogs
import json,time,datetime
from django.template.context_processors import request
from blogs.com_mod.cdus_my import chat_add,pytitle_update
from com_dbs.models import blogs_chat
from blogs.com_mod.com_mod import CJSONEncoder
from blogs.com_mod.comment_operate import commentcla,title_pycla
from com_dbs.models import comment_python

# Create your views here.

def data_get(request):
    res={}
    curuser=request.session.get('curuser','admin')
    res['curuser']=curuser
    res['data_blogs']=comcon_blogs(request)
    res['stru_cont']=python_content(request)[0]
    res['cont_tit']=python_tit(request)[0]
    res['chat_data']=chat_select(request)
    comm=commentcla()
    res['commentpy']=comm.commstru_data(commtitle=res['cont_tit'])
    res['commnum']=comm.commcount(res['cont_tit'])
    return res

def comdata_get(request):
    res={}
    curuser=request.session.get('curuser','admin')
    res['curuser']=curuser
    res['data_blogs']=comcon_blogs(request)
    res['stru_cont']=python_content(request)[0]
    res['cont_tit']=python_tit(request)[0]
    res['chat_data']=chat_select(request)
    comm=commentcla()
    res['commentpy']=comm.commstru_data(commtitle=res['cont_tit'])
    res['commnum']=comm.commcount(res['cont_tit'])
    print res['commentpy']
    return res

def blogs(request):
    if request.session.get('login',False):
        curuser=request.session.get('curuser','admin')
        if curuser=='guan':
            request.session['cur_stru_title']='python2'
            res=data_get(request)
            return render_to_response('blogs/blogs_super.html',res)
        else:
            request.session['cur_stru_title']='python2'
            res=data_get(request)
            return render_to_response('blogs/blogs.html',res)
    else:
        return redirect('/login/')
#     return render_to_response('blogs/blogs.html',res)
def blog_cont_ajax(request):
    res={}
    cur_title=request.POST.get('dat','Python2')
    request.session['cur_stru_title']=cur_title
    pytitle=python_tit(request)[0]
    res['cont_title']=pytitle.title
    res['cont_visit']=pytitle.visit_count
    res['cont_date']=str(pytitle.note_date).split('+')[0]
    res['cont_content']=python_content(request)[0].cont_py
    comm=commentcla()
    res['commentpy']=comm.commstru_ajaxdata(commtitle=pytitle)
    res['commnum']=comm.commcount(pytitle)
    return HttpResponse(json.dumps(res,cls=CJSONEncoder))

def webchat_increment(request):
    chatincre={}
    lastid=request.session.get('chat_lastid',1)
    chat_incre=blogs_chat.objects.filter(id__gt=lastid).order_by('-id')
    if chat_incre.count() == 0:
        chatincre['data_st']=0
    else:
        chatincre['chat_incre']=list(reversed(chat_incre.values()))
        chatincre['data_st']=1
        request.session['chat_lastid']=chat_incre[0].id
    return HttpResponse(json.dumps(chatincre,cls=CJSONEncoder))

def webchat_adddata(request):
    chatres={}
    chatres['time_now']=time.strftime('%Y-%m-%d %H:%M:%S')
    chatres['curuser']=request.session.get('curuser','admin')
    chatres['chatcont']=request.POST['dat']
    chatres['msg']=chat_add(request, username=chatres['curuser'], chat_cont=chatres['chatcont'])
    if chatres['msg']==1:
        request.session['chat_lastid']=blogs_chat.objects.filter(username=chatres['curuser'], chat_cont=chatres['chatcont'])[0].id
    return HttpResponse(json.dumps(chatres))

def adddata(request):
    tablename=user
    filehtml='blogs/add_data.html'
    return madddata(request,tablename, filehtml)

def comment_py(request):
    commres={}
    commres['commdate']=time.strftime('%Y-%m-%d %H:%M:%S')
    commres['commuser']=request.session.get('curuser','admin')
    commres['commcont']=request.POST['dat']
    commres['commtitle']=request.session.get('cur_stru_title','python2.7')
    pyt=title_pycla()
    title=pyt.pytitle_select(commres['commtitle'])
    commres['commlevel']=1
    commres['commreply']='0'
    comm=commentcla()
    commres['msg']=comm.commadd(commuser=commres['commuser'], commcont=commres['commcont'], commreply=commres['commreply'], commlevel=commres['commlevel'], commtitle=title)
    return HttpResponse(json.dumps(commres))

def reply_submit(request):
    replyres={}
    replyres['replydate']=time.strftime('%Y-%m-%d %H:%M:%S')
    replyres['curuser']=request.session.get('curuser','admin')
    replyres['replycont']=request.POST['cont']
    replyres['replytitle']=request.session.get('cur_stru_title','python2.7')
    pt=title_pycla()
    title=pt.pytitle_select(replyres['replytitle'])
    replyres['replypredate']=request.POST['timeobj']
    replyres['replyuser']=request.POST['userobj']
    comm=commentcla()
    replyres['replylevel']=comm.replyselect(commtitle=replyres['replytitle'], commuser=replyres['replyuser'], commdate=replyres['replypredate'])[0].comment_level
    if replyres['replylevel'] < 3:
        replyres['replylevel']=replyres['replylevel']+1
    else:
        replyres['replylevel']=replyres['replylevel']
    replyres['msg']=comm.replyadd(commuser=replyres['curuser'], commcont=replyres['replycont'], commreply=replyres['replyuser'], commlevel=replyres['replylevel'], commtitle=title,commpredate=replyres['replypredate'])
    return HttpResponse(json.dumps(replyres))

def curblogs(request):
    res={}
    res['cur_obj']=request.session['cur_stru_title']
    return HttpResponse(json.dumps(res))

def blogs_obj(request,obj):
    if request.session.get('login','False'):
        curuser=request.session.get('curuser','admin')
        if curuser=='guan':
            request.session['cur_stru_title']=obj
            res=comdata_get(request)
            return render_to_response('blogs/blogs_super.html',res)
        else:
            request.session['cur_stru_title']=obj
            res=comdata_get(request)
            return render_to_response('blogs/blogs_com.html',res)
    else:
        return redirect('/login/')
    
def visitnum(request):
    res={}
    title=request.POST['dat']
    res['msg']=pytitle_update(request, title)
    
    return HttpResponse(json.dumps(res))
    
def sorryservice(request):
    return render_to_response('blogs/sorry_server.html')
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    

