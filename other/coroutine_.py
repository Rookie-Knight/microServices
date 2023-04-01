# -*- coding: utf-8 -*-

import asyncio

import requests


@asyncio.coroutine
def download(url):
    print('%s is downloding...' % url)
    yield from asyncio.sleep(1)
    resp = requests.get(url)
    return resp.content, resp.status_code


@asyncio.coroutine
def write_file(file_name, content):
    yield from asyncio.sleep(1)
    with open("./" + file_name, "wb") as f:
        f.write(content)

    print(file_name, "write done")


@asyncio.coroutine
def save(url, file_name):

    content, code = yield from download(url)
    print(url, code)
    yield from write_file(file_name, content)
    print(url, file_name, 'save successfully')

if __name__ == '__main__':
    # 创建事件循环器对象
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        save("https://www.baidu.com", "baidu.html"),
        save("https://www.taobao.com", "taobao.html")
    ]))