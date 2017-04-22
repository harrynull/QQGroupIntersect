# QQGroupIntersect

一个可以查看两个或多个QQ群成员交集的工具。

A tool that can get the intersection of members of two or more qq groups.


## 用法

``python ./main.py <COOKIE: uin> <COOKIE: skey> <COOKIE: p_skey> <Group ID ...>``

Python 3.5.2测试通过，需要安装``requests``依赖库。

## 常见问题
* 怎么才能找到Cookie?

  登录http://qun.qq.com，然后找cookie。

* 为什么输出的时候提示``UnicodeEncodeError: 'gbk' codec can't encode character '\x**' in position ***``

  Windows下控制台用的是gbk编码。请把print改成输出到utf-8编码的文件里。或者使用支持utf-8编码的控制台。

* 为什么提示``Failed to get group members. Received json: {'ec': 1, 'em': 'no&nbsp;login'}``

  请检查cookie是正确的。如果cookie内有特殊符号需要用双引号括起来。


## 许可证
代码许可证：MIT License
