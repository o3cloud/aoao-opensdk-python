# _*_ coding: utf-8 _*_
from .base import AoaoBase
from .http_client import RequestsClient


class AoaoBasic(AoaoBase, RequestsClient):
    """嗷嗷基本功能类

    :param access_key: 公钥（ 由嗷嗷对接人员提供 )，用于数据传输，及身份验证
    :param secret_key: 私钥（ 由嗷嗷对接人员提供 )，用于计算签名
    """

    def __init__(self, access_key=None, secret_key=None):
        super(AoaoBasic, self).__init__(access_key, secret_key)

    def create(self, org_id, org_order_id, contract_id, pay_type, city_code, org_order_pushed_at=None,
               shipping_date=None,
               shipping_time=None, goods=None, total_weight=None, total_volume=None, barcode=None,
               preserve_mode=None, note=None, pickup_code=None, recv_code=None, order_amonut=None, cod_amonut=None,
               pay_amount=None, extra_metas=None, address_id=None, consignor=None,
               ):
        """嗷嗷下单接口

        商户可通过此接口向嗷嗷平台推送订单，平台接收到请求后会立即告知订单是否接收成功，然后会通过推送接口告知订单的实时状态

        注：
            1.地址 ID ( address_id ) 与发货信息 ( consignor ) 只能二选一，如果两者都存在则以 consignor 为准；
            2.如果在嗷嗷平台中订单已经为关闭状态，则可以重新推送此订单，org_order_id 和 barcode 可以重复使用。

        :param kwargs:
        :return:
        """

        cmd = 'aoao.o2o.order.create'

        body = {
            'org_id': org_id,
            'org_order_id': org_order_id,
            'contract_id': contract_id,
            'pay_type': pay_type,
            'city_code': city_code,
        }

        data = self.get_aoao_object(cmd, **body)
        r = self.request(data)
        return r
