#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
"""
更新用户信息
"""

keyword = u"美女"      # 搜索内容
offset = "0"         # 偏移位置

# 获取Token       有效期60分钟
token = getToken()
# 获取新的设备信息  有效期永久
#device_info = getDevice()

# 当前用户的设备信息
device_info = {
    'iid': '',
    'idfa': '',
    'vid': '',
    'device_id': '',
    'openudid': '',
    'device_type': 'iPhone8,1',
    'os_version': '10.2',
    'os_api': '18',
    'screen_width': '750',
    'device_platform': 'iphone'
}

# 当前用户的Cookie
header['Cookie'] = ""

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
    "ac":       "WIFI",
    "count":    "12",
}

post_params = {
    'signature': '.........:)'
}

sign_params = params.copy()
sign_params.update(post_params)

sign = getSign(token, sign_params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = requests.post("https://aweme.snssdk.com/aweme/v1/commit/user/", params=params, data=post_params, headers=header).json()
print(resp)

