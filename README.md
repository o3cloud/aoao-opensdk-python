# aoao-opensdk-python
Python sdk for aoao open api

## 概述
aoao-opensdk-python 封装了嗷嗷系统开放接口调用方法，本开发包目前支持嗷嗷下单接口、订单查询接口、订单取消接口。

## 安装


## 组件说明
aoao-opensdk-python 有一个主要组件：AoaoBasic。它是嗷嗷基本功能类，与[嗷嗷开放平台OpenApi接口文档](http://docs.o3cloud.cn/v3/)对应。是对该文档所有接口的二次封装，方便调用。


## 快速开始
在开始之前，请准备好你的：

* access_key: 公钥（由嗷嗷对接人员提供），用于数据传输，及身份验证）
* secret_key: 私钥（ 由嗷嗷对接人员提供 )，用于计算签名
* org_id: 商家ID（可在嗷嗷PC端获取）

### 实例化嗷嗷基本功能类

```
    from aoao_sdk import AoaoBasic
    aoao = AoaoBasic(
        access_key='your access key',
        secret_key='your secret key',
        org_id='your org id'
        )
```

### 调用方法与示例

#### 创建订单

```
    aoao.create(
        # 必须字段
        org_order_id='37dh'  # 商家订单编号(在嗷嗷平台必须唯一)
        contract_id='582ee8322bf1d04a6fe2d420'  # 签约合同ID（目前由平台技术对接人员提供）
        pay_type=3  # 配送费支付方式，1:现金支付 2:余额支付 3:后付费
        city_code='110000' 城市编码，必须字段

        # 可选字段
        org_order_pushed_at=1482400594  # 商家订单推送时间，单位：Unix时间戳(精确到秒)
        shipping_date=20161221  # 要求送达日期，例：20161221
        shipping_time='21:00'  # 要求送达时间点，例：12:55
        goods=[
            {
                "name": "商品1",
                "specs": "500g",
                "quantity": 1,
                "price": "2300"
            }
        ]  # 商品信息
        total_weight=2500  # 总重量，单位：克
        total_volume3500  # 总体积，单位：立方厘米
        barcode=8594859  # 条码号，由字母、数字组成，在嗷嗷平台必须唯一
        preserve_mode=u'冷藏'  # 存储要求，例：冷冻
        note=u'请尽快送达'  # 备注
        pickup_code=''  # 提货码，由商家提供，骑士取货时出示
        recv_code''  # 签收码，由商家提供，顾客签收时出示
        order_amonut=2300  # 订单总金额，单位：分
        cod_amonut=0  # 代收款，单位：分，骑士代商家向顾客收取
        pay_amount=0  # 代付款，单位：分，骑士代商家向供货方垫付货款
        address_id='582eee402bf1d04b56a369fa'  # 嗷嗷平台地址ID（可通过嗷嗷商家PC端获取，作为发货地信息使用）
        consignor={
            "name": u"张三",
            "phone": "18288888888",
            "address": u"北京市朝阳区酒仙桥兆维华灯大厦",
            "address_detail": u"A1区321室",
            "bd_poi": [
                116.243,
                39.434
            ]
        }  # 发货信息
    )
```

#### 查询订单
商家可通过此接口查询单笔或多笔订单信息。

```
    aoao.find(
        # 可选字段
        org_order_ids=[‘123’,‘456’]  # 商家订单ID,可查询多笔
        start_date=20161201  # 开始日期, 格式：yyyymmdd
        end_date=20161201  # 结束日期, 格式：yyyymmdd
        page=2  # 当前页
        limit=20  # 每页条数, 不大于30
        detail_mode=1  # 1:只返回订单基础信息和物流信息，2:返回订单全部信息
    )
```

#### 关闭订单
商家可通过此接口取消嗷嗷平台订单;
订单只有在已创建、已确认、异常的状态下取消，其它状态不允许取消。

```
    aoao.close(
        # 必须字段
        close_note=u'顾客取消'  # 取消原因

        # 可选字段
        org_order_id='37dh'  # 商家订单ID
        order_id=''  # 平台订单ID
    )
```
