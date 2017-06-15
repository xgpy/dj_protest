#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
import urllib
from com_mod.login import logindb_chk
from models import user
from com_mod.identf_code import create_validate_code
from _io import BytesIO

# Create your views here.

def index(request):
    ret={}
    if request.session.get('login',False):
        curuser=request.session.get('curuser')
        ret['curuser']=curuser
        return render_to_response('webapp/webapp.html',ret)
    else:
        return redirect('/login/')

def login(request):
    usertable=user
    filehtml='webapp/login.html'
    return logindb_chk(request,usertable,filehtml)



def agent_api(request):
    data=request.POST
    data=json.loads(data.items()[0][0])
    print data['content']['first'].encode('utf8')
    return HttpResponse('ok')


def identf_code(request):
    f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片
    img, code = create_validate_code() #调用check_code生成照片和验证码
    request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
    img.save(f,'PNG') #生成的图片放置于开辟的内存中
    return HttpResponse(f.getvalue()) #将内存的数据读取出来，并以HttpResponse返回








