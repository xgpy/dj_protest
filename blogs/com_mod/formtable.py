#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django import forms
from blogs.com_mod.cdus_my import com_select
from webapp.models import usertype

def fun_foreign_data():
    foreign_data=[]
    data=com_select(usertype)
    for d in data:
        foreign_data.append((d.id,d.name))
    return foreign_data

class auser(forms.Form):
    usertype_data=fun_foreign_data()
    username=forms.CharField(error_messages={'required':('用户名不能为空。'),'invalid':('用户名格式错误。')},widget=forms.TextInput(attrs={'class':'userincla','placeholder':'用户名'}))
    password=forms.CharField(error_messages={'required':('密码不能为空。'),'invalid':('密码格式错误。')},widget=forms.TextInput(attrs={'class':'userincla','type':'password','placeholder':'密码'}))
    email=forms.EmailField(error_messages={'required':('邮箱不能为空。'),'invalid':('邮箱格式错误。')},widget=forms.TextInput(attrs={'class':'userincla','placeholder':'邮箱'}))
    user_type=forms.ChoiceField(choices=usertype_data,label='用户类型')
#     user_type=forms.ChoiceField(choices=usertype_data,label='用户类型',widget=forms.RadioSelect)


