# _*_ coding: utf-8 _*_
from aoao_sdk import AoaoBasic

access_key = ''
secret_key = ''
org_id = ''
aoao_sdk = AoaoBasic(access_key, secret_key, org_id)


class TestAoaoSdk(object):
    """嗷嗷sdk测试"""

    def test_create(self):
        data = {

        }
        r = aoao_sdk.create(**data)
        assert r

    def test_find(self):
        data = {

        }
        r = aoao_sdk.find(**data)
        assert r

    def test_close(self):
        data = {

        }
        r = aoao_sdk.close(**data)
        assert r
