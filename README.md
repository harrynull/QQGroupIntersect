# QQGroupIntersect

一整套用来分析QQ群成员的工具。

A tool that can analyze the intersection of members of two or more qq groups.

Python 3.5.2测试通过，需要安装``requests``依赖库。

## 用法

fetch.py <COOKIE: uin> <COOKIE: skey> <COOKIE: p_skey>
通过QQ账号获取加的所有qq群的成员数据

find.py <QQ UID> <Groups...>
通过qq号搜索ta加了什么群

merge.py <Name> <Groups...>
合并几个群的成员信息，通过这个生成的数据是和普通群数据等价的，可以用在所有能用普通数据的地方(Groups...)

compare.py <Groups...>
比较几个群的成员信息，找出同时加了几个群的成员

## 例子
你想知道你加的几个编程群(a,b)和你的几个同学群(c,d,e)之间有没有交集（想来也不会有吧）：
```
    python3 fetch.py
    python3 merge.py prog a b
    python3 merge.py stu c d e
    python3 compare.py prog stu
```
然后你发现竟然真的有一个人A同时加了两个群，但是你发现你其实不认识A，你就可以：
```
    python3 find.py A a b c d e
```
这样就可以找到A加了哪些群，以及ta用的昵称


## 常见问题
* HTTP 501

  已知问题，请更换fetch.py中的User-Agent。

* 怎么才能找到Cookie?

  登录http://qun.qq.com，然后找cookie。

* 为什么输出的时候提示``UnicodeEncodeError: 'gbk' codec can't encode character '\x**' in position ***``

  Windows下控制台用的是gbk编码。请把print改成输出到utf-8编码的文件里。或者使用支持utf-8编码的控制台。

* 为什么提示``Failed to get group members. Received: {'ec': 1, 'em': 'no&nbsp;login'}``

  请检查cookie是正确的。如果cookie内有特殊符号需要用双引号括起来。


## 许可证
代码许可证：MIT License
