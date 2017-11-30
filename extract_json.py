#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:48:52 2017

@author: adam
"""

import json
from pprint import pprint
import os
import re
import glob
import pandas as pd

#==============================================================================
# with open('data.json') as data_file:    
#     data = json.load(data_file)
#==============================================================================
    

def extract_one_file(json_path):
    json_clean = {}
    instagram_path = 'www.instagram.com/p'
    with open(json_path) as data_file:    
        data = json.load(data_file)
    
    url = os.path.join(instagram_path,data['shortcode'])
    like_count = data['edge_media_preview_like']['count']
    comment_count = data['edge_media_to_comment']['count']
    comment_text= []
    comment_user = []
    for item in data['edge_media_to_comment']['edges']:
        comment_user.append(item['node']['owner']['username'])
        comment_text.append(item['node']['text'])
    #comment_user_list = [{'user' : item['node']['owner']['username'],'comment':item['node']['text']} for item in data['edge_media_to_comment']['edges']]
    media = data['display_url']
    caption = data['edge_media_to_caption']['edges'][0]['node']['text']
    hashtag = re.findall(r"#(\w+)", caption)
    instagram_id = data['owner']['username']
    instagram_alias = data['owner']['full_name']
    json_clean['url']=url
    json_clean['like_count'] = like_count
    json_clean['comment_count'] = comment_count
    json_clean['comment_acount'] = comment_user
    json_clean['comment_text'] = comment_text
    json_clean['media'] = media
    json_clean['caption'] = caption
    json_clean['hashtag'] = hashtag
    json_clean['instagram_id'] = instagram_id
    json_clean['instagram_alias'] = instagram_alias
    return json_clean


def extract_from_folder(json_folder_path):
    json_list = glob.glob(json_folder_path+'/*')
    json_list = []
    for json_file in json_list:
        json_list.append(extract_one_file(json_file))
        
    return json_list

if __name__ == '__main__':
    json_file = 'data.json'
    filename = 'tes.xlsx'
    #json_folder = 'pki_2017_09'
    json1 = extract_one_file(json_file)
    #json_folder = extract_from_folder(json_folder)
    df = pd.DataFrame({k : pd.Series(v) for k, v in json1.iteritems()})
    df.to_excel(filename)
           


    
#==============================================================================
# instagram_path = 'www.instagram.com/p'
# post_list = []
# for post in data:
#     post_dict = {}
#     comment_list = [{'user':item['owner']['username'],'comment':item['text']}for item in post['edge_media_to_comment']['data']]
#     like = post['edge_liked_by']
#     tags = post['tags']
#     caption = post['edge_media_to_caption']['edges'][0]['node']['text']
#     media = post['urls']
#     url = os.path.join(instagram_path,post['shortcode'])
#     
#     post_dict['comment'] = comment_list
#     post_dict['like'] = like
#     post_dict['tags'] = tags
#     post_dict['caption'] = caption
#     post_dict['media'] = media
#     post_list.append(post_dict)
#==============================================================================
    
    
#instagram-scraper --tag pki -m 100 -t image --comments --media-metadata
