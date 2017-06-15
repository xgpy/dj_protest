#!/usr/bin/python278
# -*- coding: utf-8 -*-

import json,datetime
from datetime import date

def str_int(s1,d1):
    try:
        i1=int(s1)
    except Exception:
        i1=d1
    return i1
    
class CJSONEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,obj)
        