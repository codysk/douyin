#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
"""
拉取首页视频
/aweme/v1/general/search/?iid=11111&idfa=11111-111-11-1111-1111&version_code=2.0.0&device_type=iPhone8,0&channel=App%20Store&os_version=11.0&screen_width=1334&vid=111-111-111-11-1&device_id=11111&os_api=18&app_name=aweme&build_number=20005&device_platform=iphone&app_version=2.0.0&ac=WIFI&aid=1128&openudid=1111&count=12&keyword=美女&offset=0&mas=1111&as=1111&ts=1535730343 HTTP/1.1
Host: api.amemv.com
User-Agent: Aweme/2.0.0 (iPhone; iOS 8.3; Scale/2.00)
"""

keyword = u"美女"      # 搜索内容
offset = "0"         # 偏移位置

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
    "ac":       "WIFI",
    "count":    "12",
    "keyword":  keyword,
    "offset":   offset
}
sign = getSign(token, params)
params['mas'] = sign['mas']
params['as']  = sign['as']
params['ts']  = sign['ts']
print(params)

resp = requests.get("https://api.amemv.com/aweme/v1/general/search/", params=params, headers=header).json()
print(resp)

