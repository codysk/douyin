#!/usr/bin/env python
# encoding: utf-8
import requests
from common import *
"""
QQ授权登录
"""

# 获取Token       有效期60分钟
token = getToken()
# 获取新的设备信息  有效期永久
device_info = getDevice()

dysession = requests.session()      # 登录后需要维持会话

# 拼装参数
common_params = {
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
    "ac":           "WIFI"
}

get_params = {
    "pass-region": 1
}

get_params.update(common_params.copy())        # GET类型业务参数 和 公共参数拼接在一起

post_params = {
    "access_token": "xxxxxxxxxxxxxxxxxxxxx",
    "expires_in": "********",
    "openid": "xxxxxxxxxxxxxxxxxxxxx",
    "platform": "qzone_sns"
}

sign_params = get_params.copy()
sign_params.update(post_params.copy())         # 签名参数 GET类型参数 和 POST类型参数拼接在一起

sign = getSign(token, sign_params)
get_params['mas'] = sign['mas']
get_params['as']  = sign['as']
get_params['ts']  = sign['ts']
print(get_params)

# 通过QQ授权登录
resp = dysession.post("https://lf.snssdk.com/passport/auth/login/", params=get_params, data=post_params, headers=header).json()
print(resp)


get_params = {

}

get_params.update(common_params.copy())
sign_params = get_params
sign = getSign(token, sign_params)
get_params['mas'] = sign['mas']
get_params['as']  = sign['as']
get_params['ts']  = sign['ts']
print(get_params)

# 登录后获取个人信息
resp = dysession.get("https://aweme.snssdk.com/aweme/v1/user/", params=get_params, headers=header).json()
nickname = resp['user']['nickname']
user_id = resp['user']['uid']
print("nickname: {} userid: {}".format(nickname, user_id))

dysession.get()
