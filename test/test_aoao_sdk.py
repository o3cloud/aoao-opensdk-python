# _*_ coding: utf-8 _*_
import json
from aoao_sdk import AoaoBasic

access_key = '8dfd157ac0c7250366dcbc6070847425'
secret_key = '44766ec98abf50caf01517469340b8ba'
org_id = '586f0d14998269534ae1bd72'  # 花 + seller_id
aoao_sdk = AoaoBasic(access_key, secret_key, org_id)


class TestAoaoSdk(object):
    """嗷嗷sdk测试"""

    def test_create(self):
        r = aoao_sdk.create(org_order_id='3275347', contract_id='586f3283998269534ae32c00', pay_type=3,
                            city_code='110000', org_order_pushed_at=1480599893, shipping_date=20161203,
                            shipping_time='12:00', barcode='3275347', order_amonut=0,
                            goods=[{"name": u"花＋的鲜花", "price": 100000, "extra_metas": [], "specs": u"盒",
                                    "quantity": 1}],
                            consignor={"name": u"张聪", "phone": "18501908697", "bd_poi": [
                                116.34264501279, 40.0753642287988],
                                       "address": "北京市昌平区回龙观龙博苑一区三号楼底商"},
                            consignee={"name": u"张萌", "mobile": "13466318165", "bd_poi": [116.328751, 40.077565],
                                       "address": "北京市龙泽苑西区15号楼3单元402"})
        assert r
        #
        # def test_find(self):
        #     r = aoao_sdk.find()
        #     json.loads(r.content)
        #     assert r

        # def test_close(self):
        #     data = {
        #
        #     }
        #     r = aoao_sdk.close(**data)
        #     assert r
