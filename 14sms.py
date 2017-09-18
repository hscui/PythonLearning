# coding=utf-8
from alidayu import AlibabaAliqinFcSmsNumSendRequest
import json

APPKEY = "23653262"
SECRET = "c183a3e926c6b77c49ec8e840739017e"
URL = 'https://eco.taobao.com/router/rest'

req = AlibabaAliqinFcSmsNumSendRequest(APPKEY, SECRET, URL)

req.format = "json"
req.extend = ""
req.sms_type = "normal"
req.sms_free_sign_name = "Cuis为您服务"
req.sms_param = json.dumps({"name": "hscui",
                            'time': "2017"})  # 参数字典，根据模板的实际情况填写。我的是 尊敬的 ${name}，收到这条短信说明 API 测试成功。
req.rec_num = "13416295490"
req.sms_template_code = "SMS_49460113"

try:
    resp = req.getResponse()
    print(resp)
except Exception as e:
    print(e)
