#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from com_mod.formmod import formsuser
from django.template.context import RequestContext
import md5

def logindb_chk(request,usertable,filehtml):
    res={'data':None,'error':'','name':'GUAN'}
    res['data']=formsuser()
    if request.method=='POST':
        checkform=formsuser(request.POST)
        checkresult=checkform.is_valid()
        if checkresult:
            chk_usernm=checkform['username'].value()
            chk_passwd=checkform['password'].value()
            chk_identf=request.POST['check_code'].lower()
            identfcode=request.session.get('check_code').lower()
            m=md5.md5(chk_passwd)
            chk_passwd=m.hexdigest()
            db_usernm=usertable.objects.filter(username=chk_usernm,password=chk_passwd).count()
            if db_usernm>=1:
                if chk_identf==identfcode:
                    request.session['login']=True
                    request.session['curuser']=chk_usernm
                    #return render_to_response('webapp/webapp.html')
                    return redirect('/blogs/')
                else:
                    request.session['login']=False
                    res['error']='验证码有误'
                    res['data']=checkform
                    return render_to_response(filehtml,res)
            else:
                request.session['login']=False
                res['error']='用户名或密码有误'
                res['data']=checkform
                return render_to_response(filehtml,res)
        else:
            firerrmsg=checkform.errors.as_data().values()[0][0].message
            res['error']=firerrmsg
            res['data']=checkform
            return render_to_response(filehtml,res)
    #context_instance=RequestContext(request):跨站请求伪造携带token
    return render_to_response(filehtml,res,context_instance=RequestContext(request))

def mlogout(request):
    try:
        del request.session['login']
        del request.session['curuser']
    except Exception:
        pass
    return redirect('/login/')









