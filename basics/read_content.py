# -*- coding: utf-8 -*-
"""
@Author  : Wong Jan Wei
@Time    : 2019-07-10 16:06
@File    : read_content.py
@describe: 获取响应内容
"""
import asyncio
import aiohttp


async def read_content():
    async with aiohttp.ClientSession() as session:
        async with session.get(url='http://api.github.com/events') as resp:
            print(resp.status)
            print(await resp.text())
            print(await resp.json())

            """
            虽然方法read(),json(),text()都非常方便，您应该谨慎使用它们。
            所有这些方法都将整个响应加载到内存中。
            例如，如果要下载几千兆字节大小的文件，这些方法将加载内存中的所有数据。
            相反，您可以使用该content属性。它是aiohttp.StreamReader的一个实例。在gzip和deflate转移编码自动进行解码.
            """
            async with session.get('https://api.github.com/events') as resp:
                await resp.content.read(10)
            # 但是，一般情况下，您应该使用这样的模式来保存流式传输到文件的内容：
            with open("./test.bin", 'wb') as fd:
                while True:
                    chunk = await resp.content.read(1024)
                    if not chunk:
                        break
                    fd.write(chunk)


if __name__ == '__main__':
    asyncio.run(read_content())
