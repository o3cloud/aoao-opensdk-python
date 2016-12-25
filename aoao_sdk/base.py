# _*_ coding: utf-8 _*_
import json
import uuid
import time
import hmac
import hashlib
from . import version


class AoaoBase(object):
    """嗷嗷sdk功能基类

    :param access_key: 公钥（ 由嗷嗷对接人员提供 )，用于数据传输，及身份验证
    :param secret_key: 私钥（ 由嗷嗷对接人员提供 )，用于计算签名
    """
    def __init__(self, access_key=None, secret_key=None):
        self.access_key = access_key
        self.secret_key = secret_key
        pass

    def get_aoao_object(self, cmd, **kwargs):
        """转换为嗷嗷协议

        :param cmd:
        :param kwargs:
        :return:
        """
        types = {
            'access_key': self.access_key,
            'body': kwargs,
            'cmd': cmd,
            'ticket': str(uuid.uuid1()).upper(),
            'version': version.version,
            'time': int(time.time()),
        }
        json_data = json.dumps(types, ensure_ascii=True, default=str, separators=(',', ':'),
                               sort_keys=True)
        result = hmac.new(self.secret_key, json_data, hashlib.md5).hexdigest()
        types['sign'] = result
        return json.dumps(types)

    @staticmethod
    def check_dictvalue(need_keys, **kwarg):
        """检测必须字段

        :param need_keys:
        :param kwarg:
        :return:
        """
        result = True
        for key in need_keys:
            if key in kwarg and kwarg[key] is not None and kwarg[key] != '':
                continue
            else:
                return json.dumps({"message": "parameter error <{0}> ".format(key)})
        return result
