---
sidebar_position: 0
---

# python

### basic

```python
# json
json.dumps(item, ensure_ascii=False, indent=4)

# jmespath
https://jmespath.org/tutorial.html

# random
random.shuffle(_list)

# 对字典排序
sorted(_dict.items(), key=lambda d: d[1], reverse=False)

# unicode replace
repr()

### http server
py2 python -m SimpleHTTPServer 8000
py3 python -m http.server 8000

# 格式化输出
print("{:02d}".format(1))
print(f"{1:02d}")

# 乘法表
print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
```

### decorator try

```python
import functools

def decorator_try(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            return err

    return wrapper
```

### [datetime](https://docs.python.org/zh-cn/3/library/datetime.html#datetime.timezone)

```python
pip install python-dateutil

# datetime to timestamp
import datetime
d = datetime.date(2023, 1, 1)
print(d)
print(d.strftime("%s"))

# timestamp to datetime
from datetime import datetime
timestamp = 1694691579999
dt_object = datetime.fromtimestamp(timestamp/1000)
print("dt_object =", dt_object)

# yestoday
from datetime import datetime, timedelta

# days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
yestoday = datetime.today() - timedelta(days=1)
print(yestoday)

from datetime import datetime
from dateutil import parser

format_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

t = "Thu, 9 Sep 2021 00:17:59"
result = parser.parse(t)
print(result)
print(type(result))

now = datetime.now()
print((now - result).days)

>>> import arrow
>>> arrow.get('2013-05-11T21:23:58.970460+07:00')
<Arrow [2013-05-11T21:23:58.970460+07:00]>

>>> utc = arrow.utcnow()
>>> utc
<Arrow [2013-05-11T21:23:58.970460+00:00]>

>>> utc = utc.shift(hours=-1)
>>> utc
<Arrow [2013-05-11T20:23:58.970460+00:00]>

>>> local = utc.to('US/Pacific')
>>> local
<Arrow [2013-05-11T13:23:58.970460-07:00]>

>>> local.timestamp()
1368303838.970460

>>> local.format()
'2013-05-11 13:23:58 -07:00'

>>> local.format('YYYY-MM-DD HH:mm:ss ZZ')
'2013-05-11 13:23:58 -07:00'

>>> local.humanize()
'an hour ago'

>>> local.humanize(locale='ko-kr')
'한시간 전'
```

### read big file

```python
with open("log.txt") as infile:
    for line in infile:
        do_something_with(line)
```

### iterator

```python
def generate_iterator():
    for i in range(10):
        yield i


for i in generate_iterator():
    print(i)

# num = generate_iterator()
# while True:
#     try:
#         print(next(num))
#     except StopIteration:
#         print('stop')
#         break
```

### csv

```python
import csv

# read
result = []
input_file = csv.DictReader(open("result.csv"))
for row in input_file:
    result.append(row)
print(result)


# write dict
my_dict = {"test": 1, "testing": 2}
with open('mycsvfile.csv', 'w', encoding="utf-8-sig") as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)

# write list
result = [{"test": 1, "testing": 2}, {"test": 1, "testing": 2}]
with open('mycsvfile.csv', 'w', encoding="utf-8-sig") as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, result[0].keys())
    w.writeheader()
    w.writerows(result)
```

### execl

```python
# write
pip install pandas openpyxl

# dict
import pandas as pd
df = pd.DataFrame.from_dict({'Column1':[1,2,3,4],'Column2':[5,6,7,8]})
df.to_excel('test.xlsx', header=True, index=False)

# list
import pandas as pd
Column1 = [1,2,3,4]
Column2 = [5,6,7,8]
df = pd.DataFrame.from_dict({'Column1':Column1,'Column2':Column2})
df.to_excel('test.xlsx', header=True, index=False)

# read
import pandas as pd

df = pd.read_excel("example.xlsx", index_col=0)
data_dict = df.to_dict("records")
print(data_dict)
```

### asyncio

```python
import asyncio
import time

def now(): return time.time()

async def do_some_work(x):
    print('Waiting: ', x)

    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)


# yield
def create_generator(_range):
    for i in range(_range):
        yield i

result = create_generator(5)
for i in result:
    print(i)
```

### xmljson

```python
import xmljson
from lxml.etree import  fromstring,tostring

json.loads(json.dumps(xmljson.badgerfish.data(fromstring(con.encode()))))
```

### mysql

```python
# install mysql-clients

# in archlinux
sudo pacman --noconfirm -S mysql-clients gcc
pip install mysqlclient

# mac
brew install mysql-client
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
pip install mysqlclient
```

### 转码

```python
import os
import chardet


def trans(filename):
    print("file=====", filename)
    with open(f"txt/{filename}", "rb") as file:
        con = file.read()
    _char = chardet.detect(con)["encoding"]
    print("char is ", _char)

    if "utf-8" in _char or "UTF-8" in _char:
        cmd = f"mv txt/{filename} result/{filename}"
    else:
        cmd = f"iconv -c -f {_char} -t UTF-8 txt/{filename} > result/{filename}"
    print(cmd)
    os.system(cmd)


def main():
    txts = os.listdir("txt")
    for txt in txts:
        if ".txt" not in txt:
            print(txt)
            continue
        try:
            trans(txt)
        except Exception as err:
            print(err)
        continue


if __name__ == "__main__":
    main()
```

### 省市分割

```python
pip install cpca
result = cpca.transform("xx省xx市xx区", pos_sensitive=True).to_dict("list")
```

### spider 编码

```python
# response.encoding 从网页响应的header中，提取charset字段中的编码。若header中没有charset字段，则默认为ISO-8859-1编码模式，ISO-8859-1编码无法解析中文，这也是中文乱码的原因。
# response.apparent_encoding  从网页的内容中（html源码）中分析网页编码的方式。所以apparent_encoding比encoding更加准确，获取到的才是原网页的实际编码。

response.encoding = response.apparent_encoding
print(response.encoding)
print(response.apparent_encoding)

html = etree.HTML(text)
names = html.xpath("//tr//td//text()")
names = [i.encode("iso-8859-1", "ignore").decode("gb2312", "ignore") for i in names]
```
