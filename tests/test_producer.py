# -*- coding: utf-8 -*-
from rocketmq.client import Message, SendStatus


def test_producer_send_sync(producer):
    msg = Message('test')
    msg.set_keys('send_sync')
    msg.set_tags('XXX')
    msg.set_body('XXXX')
    ret = producer.send_sync(msg)
    assert ret.status == SendStatus.OK


def test_producer_send_async(producer):
    msg = Message('test')
    msg.set_keys('send_async')
    msg.set_tags('XXX')
    msg.set_body('XXXX')
    producer.send_async(msg, None, None)


def test_producer_send_oneway(producer):
    msg = Message('test')
    msg.set_keys('send_oneway')
    msg.set_tags('XXX')
    msg.set_body('XXXX')
    producer.send_oneway(msg)


def test_producer_send_oneway_orderly(producer):
    msg = Message('test')
    msg.set_keys('send_oneway_orderly')
    msg.set_tags('XXX')
    msg.set_body('XXXX')
    producer.send_oneway_orderly(msg, 1)


def test_producer_send_orderly(producer):
    msg = Message('test')
    msg.set_keys('send_orderly')
    msg.set_tags('XXX')
    msg.set_body('XXXX')
    ret = producer.send_orderly(msg, 1)
    assert ret.status == SendStatus.OK
