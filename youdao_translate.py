#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 10:55:45 2021

@author: hannahbannq
"""
import json

import requests

trait = []
with open("/555traitwords.txt", "r") as f: 
    for line in f.readlines():
        line = line.strip('\n')  
        trait.append(line)
    print(trait)


#  translation function, word  content that needs to be translated 
def translate(word):
    #  youdao dictionary api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    #  the transmitted parameter, where  i  for the content that needs to be translated 
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key  this dictionary 
    response = requests.post(url, data=key)
    # 
    if response.status_code == 200:
        # 
        return response.text
    else:
        print("")
        # 
        return None

def get_reuslt(repsonse):
    #  json.loads  json 
    result = json.loads(repsonse)
    print ("%s" % result['translateResult'][0][0]['src'])
    print ("%s" % result['translateResult'][0][0]['tgt'])

def main():
    print("API")
    print("-->")
    print("-->")
    word = input('')
    list_trans = translate(word)
    get_reuslt(list_trans)
    
if __name__ == '__main__':
    main()

translation = []    
for word in trait:
    trans = translate(word)
    translation.append(trans)
get_reuslt(translate('frank'))
    
    
    