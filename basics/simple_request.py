# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei
@Time    : 2019-07-10 14:46
@File    : simple_request.py
@describe: 基本请求
"""
import asyncio
import aiohttp


async def simple_request() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())

        async with session.post(url='http://httpbin.org/post', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())

        async with session.put(url='http://httpbin.org/put', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())

        async with session.delete(url='http://httpbin.org/delete', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())

        async with session.head(url='http://httpbin.org/get', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())

        async with session.options(url='http://httpbin.org/get', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())

        async with session.patch(url='http://httpbin.org/patch', data=b"data") as resp:
            print(resp.status)
            print(await resp.text())


"""
注意
不要为每个请求创建会话。很可能每个应用程序都需要一个会话来完成所有请求。
更复杂的情况可能需要每个站点一个会话，例如一个用于Github，另一个用于Facebook API。无论如何，为每个请求进行会话是一个非常糟糕的主意。
会话内部包含连接池。连接重用和保持活动（两者都默认打开）可以加快总体性能。
"""

if __name__ == '__main__':
    asyncio.run(simple_request())
