# _*_ coding: utf-8 _*_
from aoao_sdk import AoaoBasic

access_key = ''
secret_key = ''
aoao_sdk = AoaoBasic(access_key, secret_key)


class TestAoaoSdk(object):
    """嗷嗷sdk测试"""

    def test_create(self):
        data = {

        }
        r = aoao_sdk.create(**data)
        assert r
