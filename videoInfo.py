#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
import json
import re
"""
拉取视频信息
"""

# 获取Token       有效期60分钟
token = getToken()
# 获取新的设备信息  有效期永久
device_info = getDevice()

share_url = 'http://v.douyin.com/doGP7L/'  # 抖音分享的短链
video_url = requests.get(share_url, headers={'User-Agent': 'Aweme/2.7.0 (iPhone; iOS 9.0.1; Scale/2.00)'}).url
pattern = 'https://www.iesdouyin.com/share/video/(.*)/'
m = re.search(pattern, video_url)
video_id = m.group(1)

# 拼装参数
params = {
    "iid":              device_info['iid'],
    "idfa":             device_info['idfa'],
    "vid":              device_info['vid'],
    "device_id":        device_info['device_id'],
    "openudid":         device_info['openudid'],
    "device_type":      device_info['device_type'],
    "os_version":       device_info['os_version'],
    "os_api":           device_info['os_api'],
    "screen_width":     device_info['screen_width'],
    "device_platform":  device_info['device_platform'],
    "version_code": APPINFO['version_code'],
    "channel":      APPINFO['channel'],
    "app_name":     APPINFO['app_name'],
    "build_number": APPINFO['build_number'],
    "app_version":  APPINFO['app_version'],
    "aid":          APPINFO['aid'],
    "ac":           "WIFI",
    "aweme_id":      video_id
}



sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

# 拉取用户个人信息
resp = requests.get("https://aweme.snssdk.com/aweme/v1/aweme/detail/", params=params, headers=header).json()
print(resp)

print("vid: ", video_id)
print("title: ", resp['aweme_detail']['desc'])
print("author: ", resp['aweme_detail']['author']['nickname'])
print("forward_count: ", resp['aweme_detail']['statistics']['forward_count'])
print("digg_count: ", resp['aweme_detail']['statistics']['digg_count'])
print("comment_count: ", resp['aweme_detail']['statistics']['comment_count'])
print("share_count: ", resp['aweme_detail']['statistics']['share_count'])
print("music: ", resp['aweme_detail']['music']['title'])
print("covers: ", resp['aweme_detail']['video']['cover']['url_list'])
print("dynamic_cover: ", resp['aweme_detail']['video']['dynamic_cover']['url_list'])
print("duration: ", resp['aweme_detail']['video']['duration'])

