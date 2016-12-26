# _*_ coding: utf-8 _*_
from .base import AoaoBase
from .http_client import RequestsClient


class AoaoBasic(AoaoBase, RequestsClient):
    """嗷嗷基本功能类

    :param access_key: 公钥（ 由嗷嗷对接人员提供 )，用于数据传输，及身份验证
    :param secret_key: 私钥（ 由嗷嗷对接人员提供 )，用于计算签名
    """

    def __init__(self, access_key=None, secret_key=None, org_id=None):
        """

        :param access_key:
        :param secret_key:
        :param org_id: 商家ID（可在嗷嗷PC端获取）
        """
        self.org_id = org_id
        super(AoaoBasic, self).__init__(access_key, secret_key)

    def create(self, org_order_id, contract_id, pay_type, city_code, org_order_pushed_at=None, shipping_date=None,
               shipping_time=None, goods=None, total_weight=None, total_volume=None, barcode=None, preserve_mode=None,
               note=None, pickup_code=None, recv_code=None, order_amonut=None, cod_amonut=None, pay_amount=None,
               extra_metas=None, address_id=None, consignor=None):
        """嗷嗷下单接口

        商户可通过此接口向嗷嗷平台推送订单，平台接收到请求后会立即告知订单是否接收成功，然后会通过推送接口告知订单的实时状态

        注：
            1.地址 ID ( address_id ) 与发货信息 ( consignor ) 只能二选一，如果两者都存在则以 consignor 为准；
            2.如果在嗷嗷平台中订单已经为关闭状态，则可以重新推送此订单，org_order_id 和 barcode 可以重复使用。

        :param org_order_id: 商家订单编号(在嗷嗷平台必须唯一)
        :param contract_id: 签约合同ID（目前由平台技术对接人员提供）
        :param pay_type: 配送费支付方式，1:现金支付 2:余额支付 3:后付费
        :param city_code: 城市编码
        :param org_order_pushed_at: 商家订单推送时间，单位：Unix时间戳(精确到秒)
        :param shipping_date: 要求送达日期，例：20161221
        :param shipping_time: 要求送达时间点，例：12:55
        :param goods: 商品信息
        :param total_weight: 总重量，单位：克
        :param total_volume: 总体积，单位：立方厘米
        :param barcode: 条码号，由字母、数字组成，在嗷嗷平台必须唯一
        :param preserve_mode: 存储要求，例：冷冻
        :param note: 备注
        :param pickup_code: 提货码，由商家提供，骑士取货时出示
        :param recv_code: 签收码，由商家提供，顾客签收时出示
        :param order_amonut: 订单总金额，单位：分
        :param cod_amonut: 代收款，单位：分，骑士代商家向顾客收取
        :param pay_amount: 代付款，单位：分，骑士代商家向供货方垫付货款
        :param extra_metas: 附加信息（扩展字段，暂不使用）
        :param address_id: 嗷嗷平台地址ID（可通过嗷嗷商家PC端获取，作为发货地信息使用）
        :param consignor: 发货信息
        :return:
        """

        cmd = 'aoao.o2o.order.create'

        body = {
            'org_id': self.org_id,
            'org_order_id': org_order_id,
            'contract_id': contract_id,
            'pay_type': pay_type,
            'city_code': city_code,
        }
        if org_order_pushed_at:
            body['org_order_pushed_at'] = org_order_pushed_at

        if shipping_date:
            body['shipping_date'] = shipping_date

        if shipping_time:
            body['shipping_time'] = shipping_time

        if goods:
            body['goods'] = goods

        if total_weight:
            body['total_weight'] = total_weight

        if total_volume:
            body['total_volume'] = total_volume

        if barcode:
            body['barcode'] = barcode

        if preserve_mode:
            body['preserve_mode'] = preserve_mode

        if note:
            body['note'] = note

        if pickup_code:
            body['pickup_code'] = pickup_code

        if recv_code:
            body['recv_code'] = recv_code

        if order_amonut:
            body['order_amonut'] = order_amonut

        if cod_amonut:
            body['cod_amonut'] = cod_amonut

        if pay_amount:
            body['pay_amount'] = pay_amount

        if extra_metas:
            body['extra_metas'] = extra_metas

        if address_id:
            body['address_id'] = address_id

        if consignor:
            body['consignor'] = consignor

        data = self.get_aoao_object(cmd, **body)
        r = self.request(data)
        return r

    def close(self, org_order_id=None, order_id=None, close_note=None):
        """订单取消接口sdk

        说明：
            1. 商家可通过此接口取消嗷嗷平台订单;
            2. 订单只有在已创建、已确认、异常的状态下取消，其它状态不允许取消。

        :param org_order_id: 商家订单ID
        :param order_id: 平台订单ID
        :param close_note: 取消原因
        :return:
        """
        cmd = 'aoao.o2o.order.close'
        body = {
            'org_id': self.org_id,
        }
        if org_order_id:
            body['org_order_id'] = org_order_id
        if order_id:
            body['order_id'] = order_id
        if close_note:
            body['close_note'] = close_note

        data = self.get_aoao_object(cmd, **body)
        r = self.request(data)
        return r
