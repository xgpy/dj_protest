#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json,datetime
import urllib
from _io import BytesIO

# Create your views here.

def hcharts(request):
    h_res={}
    h_res['name']='GUAN'
    
    return render_to_response('hcharts/hcharts.html',h_res)

def hchartsdata(request):
    hd_res=[
        [1462519800,95],
        [1462519802,48],
        [1462519803,45],
        [1462519804,38],
        [1462519805,49],
        [1462519806,62],
        [1462519807,50],
        [1462519808,30],
        [1462519809,20],
        [1462519810,20],
        [1462519811,30],
        [1462519812,10],
        [1462519813,20],
        [1462519814,30],
        [1462519815,60],
        [1462519816,50],
        [1462519817,60],
        [1462519818,20],
        [1462519819,50],
        [1462519820,30],
        [1462519821,50],
        [1462519822,60],
        [1462519823,50],
        [1462519824,70],
        [1462519825,50],
        [1462519826,60],
        [1462519827,90],
        [1462519828,50],
        [1462519829,30],
        [1462519830,80],
        [1462519831,50],
        [1462519832,50],
        [1462519833,60],
        [1462519834,90],
        [1462519835,50],
        [1462519836,80],
        [1462519837,70],
        [1462519838,70],
        [1462519839,60],
        [1462519840,50],
        [1462519841,60],
        [1462519842,50],
        [1462519843,70],
        [1462519844,50],
        [1462519845,70],
        [1462519846,70],
        [1462519847,50],
        [1462519848,30],
        ]
    
    return HttpResponse(json.dumps(hd_res))


