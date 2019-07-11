# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei
@Time    : 2019-07-10 15:03
@File    : carry_parameters.py
@describe: 请求时携带参数
"""
import asyncio
import aiohttp
from aiohttp.formdata import FormData


async def carry_parameters() -> None:
    # 可选择使用的json序列化器, 可以使用ujson,比较快,但是兼容性微差, 默认情况下，会话使用python的标准json模块进行序列化
    # async with aiohttp.ClientSession() as session:
    async with aiohttp.ClientSession() as session:
        # 多组键值对
        params = {'key1': 'value1', 'key2': 'value2'}
        # 一个key对应多个value
        params = [('key', 'value1'), ('key', 'value2')]
        async with session.get("http://httpbin.org/get", params=params) as resp:
            print(resp.status)
            print(await resp.text())

        # 携带json
        async with session.post(url='http://httpbin.org/post', json={'test': 'object'}) as resp:
            print(resp.status)
            print(await resp.text())

        # post请求携带非表单数据
        # 如果要发送非表单编码的数据，可以通过传递bytes而不是a来完成dict。此数据将直接发布，内容类型默认设置为“application / octet-stream”：
        async with session.post("http://httpbin.org/post", data=b'\x00Binary-data\x00') as resp:
            pass

        # POST多段编码文件
        # 要上传多部分编码的文件
        files = {'file': open('report.xls', 'rb')}
        async with session.post("http://httpbin.org/post", data=files) as resp:
            pass


if __name__ == '__main__':
    asyncio.run(carry_parameters())
