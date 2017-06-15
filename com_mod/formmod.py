#!/usr/bin/python278
# -*- coding: utf-8 -*-

from django import forms

class formsuser(forms.Form):
    username=forms.CharField(error_messages={'required':('用户名不能为空。'),'invalid':('用户名格式错误。')},widget=forms.TextInput(attrs={'class':'inputcla','placeholder':'用户名'}))
    password=forms.CharField(error_messages={'required':('密码不能为空。'),'invalid':('密码格式错误。')},widget=forms.TextInput(attrs={'class':'inputcla','type':'password','placeholder':'密码'}))

