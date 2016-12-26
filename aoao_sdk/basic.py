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

    def create(self, **kwargs):
        """嗷嗷下单接口

        商户可通过此接口向嗷嗷平台推送订单，平台接收到请求后会立即告知订单是否接收成功，然后会通过推送接口告知订单的实时状态

        注：
            1.地址 ID ( address_id ) 与发货信息 ( consignor ) 只能二选一，如果两者都存在则以 consignor 为准；
            2.如果在嗷嗷平台中订单已经为关闭状态，则可以重新推送此订单，org_order_id 和 barcode 可以重复使用。

        :param kwargs:
        :return:
        """
        cmd = 'aoao.o2o.order.create'
        need_params_create = [
            'org_id',
            'org_order_id',
            'contract_id',
            'pay_type',
            'consignee',
            'city_code',
        ]
        check_result = self.check_dictvalue(need_params_create, **kwargs)
        if not check_result:
            return check_result
        data = self.get_aoao_object(cmd, **kwargs)
        r = self.request(data)
        return r

    def find(self, org_id, org_order_ids=None, start_date=None, end_date=None, page=None, limit=None, detail_mode=None):
        """订单查询接口

        商家可通过此接口查询单笔或多笔订单信息

        :param org_id: 商家ID
        :param org_order_ids: 商家订单ID
        :param start_date: 开始日期, 格式：yyyymmdd, 例: 20161201
        :param end_date: 结束日期, 格式：yyyymmdd
        :param page: 当前页
        :param limit: 每页条数, 不大于30
        :param detail_mode: 1:只返回订单基础信息和物流信息，2:返回订单全部信息
        :return:
        """
        cmd = 'aoao.o2o.order.find'
        body = {
            'org_id': org_id,
        }
        if org_order_ids:
            body['org_order_ids'] = org_order_ids
        if start_date:
            body['start_date'] = start_date
        if end_date:
            body['end_date'] = end_date
        if page:
            body['page'] = page
        if limit:
            body['limit'] = limit
        if detail_mode:
            body['detail_mode'] = detail_mode

        data = self.get_aoao_object(cmd, **body)
        r = self.request(data)
        return r
