urllib2是python 2.7自带的模块，位置在 `/usr/lib/python2.7/urllib2.py`  


### 异步

#### 异常1：AttributeError: 'module' object has no attribute 'urlopen'
``` python
# -*- coding:utf-8 -*-
import urllib2

url = 'http://www.python.org/'
response = urllib2.urlopen(url)
...
```
