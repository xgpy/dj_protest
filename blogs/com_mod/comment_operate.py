#!/usr/bin/python278
# -*- coding: utf-8 -*-

from com_dbs.models import comment_python, python_title
from com_dbs.models import python_title

'''
def chat_add(request,username='',chat_cont=''):
    blogs_chat.objects.create(username=username,chat_cont=chat_cont)
def my_delete(request,tablename,id):
    tablename.objects.get(id=id).delete()
def my_update(request,tablename,id,hostname):
    obj=tablename.objects.get(id=id)
    obj.hostname=hostname
    obj.save()
def com_select(tablename):
    data=tablename.objects.all()
'''
class commentcla(object):
    def __init__(self,*args,**kargs):
        self.table=comment_python
    def commadd(self,commuser='',commcont='',commreply='',commlevel='',commtitle=''):
        self.table.objects.create(comment_user=commuser,comment_cont=commcont,comment_reply=commreply,comment_level=commlevel,comment_title=commtitle)
        return 1
    def replyadd(self,commuser='',commcont='',commreply='',commlevel='',commtitle='',commpredate=''):
        self.table.objects.create(comment_user=commuser,comment_cont=commcont,comment_reply=commreply,comment_level=commlevel,comment_title=commtitle,prereply_date=commpredate)
        return 1
    def commselect(self,commtitle):
        data=self.table.objects.filter(comment_title=commtitle)
        return data
    def replyselect(self,commtitle='',commuser='',commdate=''):
        data=self.table.objects.filter(comment_title__title=commtitle,comment_user=commuser,comment_date=commdate)
        return data
    def commcount(self,commtitle):
        num=self.table.objects.filter(comment_title=commtitle).count()
        return num
    def commstru_data(self,commtitle=''):
        comm_dic=[]
#         commtitle=python_title.objects.get(title=commtitle)
        comm_l1=self.table.objects.filter(comment_title=commtitle,comment_level=1)
        comm_l2=self.table.objects.filter(comment_title=commtitle,comment_level=2)
        comm_l3=self.table.objects.filter(comment_title=commtitle,comment_level=3)
        for c1 in comm_l1:
            d1={}
            d1[1]=c1
            d1['data']=[]
            for c2 in comm_l2:
                d2={}
                d3={}
                d2['data']=[]
                d3[3]=[]
                if c2.comment_reply==c1.comment_user and c2.prereply_date==c1.comment_date:
                    d2[2]=c2
                    for c3 in comm_l3:
                        if c3.comment_reply==c2.comment_user and c3.prereply_date==c2.comment_date:
                            d3[3].append(c3)
                    d2['data'].append(d3)
                    d1['data'].append(d2)
            comm_dic.append(d1)
        return comm_dic
    
    def commstru_ajaxdata(self,commtitle=''):
        comm_dic=[]
#         commtitle=python_title.objects.get(title=commtitle)
        comm_l1=self.table.objects.filter(comment_title=commtitle,comment_level=1)
        comm_l2=self.table.objects.filter(comment_title=commtitle,comment_level=2)
        comm_l3=self.table.objects.filter(comment_title=commtitle,comment_level=3)
        for c1 in comm_l1:
            d1={}
            t1={}
            t1['commuser']=c1.comment_user
            t1['commcont']=c1.comment_cont
            t1['commdate']=c1.comment_date
            d1[1]=t1
            d1['data']=[]
            for c2 in comm_l2:
                d2={}
                d3={}
                d2['data']=[]
                d3[3]=[]
                if c2.comment_reply==c1.comment_user and c2.prereply_date==c1.comment_date:
                    t2={}
                    t2['commuser']=c2.comment_user
                    t2['commcont']=c2.comment_cont
                    t2['commdate']=c2.comment_date
                    d2[2]=t2
                    for c3 in comm_l3:
                        if c3.comment_reply==c2.comment_user and c3.prereply_date==c2.comment_date:
                            t3={}
                            t3['commuser']=c3.comment_user
                            t3['commcont']=c3.comment_cont
                            t3['commdate']=c3.comment_date
                            d3[3].append(t3)
                    d2['data'].append(d3)
                    d1['data'].append(d2)
            comm_dic.append(d1)
        return comm_dic
    
class title_pycla(object):
    def __init__(self,*args,**kargs):
        self.table=python_title
        
    def pytitle_select(self,title):
        data=self.table.objects.get(title=title)
        return data


