#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
import json
"""
拉取用户信息
Host: aweme.snssdk.com
User-Agent: Aweme/2.7.0 (iPhone; iOS 9.0.1; Scale/2.00)
"""

# 获取Token       有效期60分钟
token = getToken()
# 获取新的设备信息  有效期永久
device_info = getDevice()

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
    "user_id":      "xxxxxxxxx" #用户userid
}

sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

# 拉取用户个人信息
resp = requests.get("https://aweme.snssdk.com/aweme/v1/user/", params=params, headers=header).json()
print(json.dumps(resp))

print("uid: ", resp['user']['uid'])
print("city: ", resp['user']['city'])
print("nickname: ", resp['user']['nickname'])
print("total_favorited: ", resp['user']['total_favorited'])
print("following_count: ", resp['user']['following_count'])
print("follower_count: ", resp['user']['follower_count'])
