# 抖音通信协议 2.9.1版本协议签名

## 简介

通过抖音通信协议实现自动化爬取抖音视频，批量注册登录，点赞，评论, 视频下载上传等功能

抖音通信协议支持抖音 iOS 2.9.1（最新）/iOS 2.8.0/2.7.0/2.0.0 版本协议，提供生成iOS设备信息功能，方便调用协议(其他版本协议请自测)

提供生成签名服务，方便对抖音通信协议进行签名。签名参数: `as`, `mas`, `ts`

因为2.7.0签名/2.8.0签名/2.9.1签名算法相同，所以可以调用API加签服务中的2.7.0的签名算法，使用对应版本的APPINFO信息即可。

项目持续更新中...

技术支持，商务合作 请联系: longhong288@outlook.com

iOS协议手机抓包操作 参考: [在 iPhone 上利用 Charles 抓包](https://www.jianshu.com/p/8825179786ac)


## 使用说明
通过调用API加签服务来完成获取新的设备信息及协议签名。

实现过程:
1. 通过访问 `https://api.appsign.vip:2688/token/douyin/version/2.7.0` 获取抖音协议2.7.0的加签token，其他版本如2.6.0，修改version后面的版本号，如果不添加/version/<版本号>参数(暂不支持，有需要可以提issus)，默认版本号为最新版本，token有效期为60分钟
2. 如果没有设备信息可以请求 `https://api.appsign.vip:2688/douyin/device/new/version/2.7.0` 获取新的设备信息，包括install_id, vid, device_id, openudid 等， 设备信息为永久使用，版本号参考token获取中的版本号设置
3. 有了设备信息和加签Token， 需要通过参数构造加签字符串，调用 `https://api.appsign.vip:2688/sign` 完成参数的加签

---

> token有效期为一个小时，支持多线程进行加签，token失效之前无需重复获取
> 设备信息依据需要进行获取

## API参数
1. 获取抖音加签Token
```
https://api.appsign.vip:2688/token/douyin  # 默认版本为最新
https://api.appsign.vip:2688/token/douyin/version/2.7.0
```
```
{
    "token":"5826aa5b56614ea798ca42d767170e74",
    "success":true
}
```

2. 生成新的设备属性
```
https://api.appsign.vip:2688/douyin/device/new  # 默认版本为最新
https://api.appsign.vip:2688/douyin/device/new/version/2.7.0
```
```
{
    "data":{
        "os_api":"23",
        "screen_width":"1334",
        "vid":"39******-ABCD-DA1D-C2C5-******995D7",
        "os_version":"11.0",
        "new_user":1,
        "install_id":4286******3,
        "iid":***********,
        "idfa":"95******-87D6-F152-04F1-88B******418",
        "device_type":"iPhone8.1",
        "device_platform":"iphone",
        "openudid":"b9f9a7c2c9******45c9aafec7b******24cc6",
        "device_id":57000******
    },
    "success":true
}
```

3. 参数加签
```
https://api.appsign.vip:2688/sign
{
    "token":"TOKEN",
    "query":"通过参数生成的加签字符串"
}
```
```
{
    "data":{
        "mas":"0041******cf******511116******1f17624******2e7******8e",
        "as":"a1a506881111aba6******",
        "ts":"153******4"
    },
    "success":true
}
```

## 登录/注册后会话维持
使用短信，或者第三方授权进行登录或者注册后，保持当前帐号的设备信息和Cookie信息，在下次需要使用指定帐号发起业务请求的时候，使用指定已经登录帐号的设备信息和Cookie发送数据包，即是使用指定帐号在登录状态下发送的请求。

**建议把登录帐号的设备信息和Cookie保持在数据库中，方便之后的使用**

## APP版本信息
针对不同版本的抖音，可以使用如下版本信息：
```
APPINFO = {
    "version_code": "2.9.1",
    "app_version": "2.9.1",
    "channel": "App Stroe",
    "app_name": "aweme",
    "build_number": "29101",
    "aid": "1128",
}

APPINFO = {
    "version_code": "2.8.0",
    "app_version": "2.8.0",
    "channel": "App Stroe",
    "app_name": "aweme",
    "build_number": "28007",
    "aid": "1128",
}

APPINFO = {
    "version_code": "2.7.0",
    "app_version": "2.7.0",
    "channel": "App Stroe",
    "app_name": "aweme",
    "build_number": "27014",
    "aid": "1128",
}

APPINFO = {
    "version_code": "2.0.0",
    "channel": "pp",
    "app_name": "aweme",
    "build_number": "20005",
    "app_version": "2.0.0",
    "aid": "1128",
}

APPINFO = {
    "version_code": "2.5.1",
    "channel": "App Store",
    "app_name": "aweme",
    "build_number": "25105",
    "app_version": "2.5.1",
    "aid": "1128",
}

APPINFO = {
    "version_code": "2.6.0",
    "channel": "App Store",
    "app_name": "aweme",
    "build_number": "26006",
    "app_version": "2.6.0",
    "aid": "1128",
}

等其他
```


## 实例

* [x] 爬取首页视频: `feed.py`
* [x] 视频搜索: `search.py`
* [x] 注册/登录 - 手机短信 `loginBySMS.py`
* [x] 注册/登录登录 - QQ授权 `loginByQQ.py`
* [ ] 点赞
* [ ] 评论
* [x] 视频下载 无水印 `downloadVideo.py`
* [ ] 视频上传
* [x] 拉取指定用户个人信息 `userInfo.py`


## 更新
* 2018.10.07 更新支持最新版2.9.1协议
* 2018.10.06 更新支持最新版2.8.0协议
* 2018.09.28 兼容之前2.0.0版本协议
* 2018.09.19 更新支持最新版2.7.0协议，~~同时兼容之前2.0.0版本协议~~
