# frp

## downloads

> https://github.com/fatedier/frp/releases

## frps

```shell
[common]
bind_port = 35000
token = xxx

dashboard_addr = 0.0.0.0
dashboard_port = 7400
dashboard_user = xxx
dashboard_pwd = xxx
```

## frpc

```shell
[common]
server_addr = address
server_port = 35000
token = xxx

use_encryption = true
use_compression = true


[some_name]
type = tcp
local_ip = localhost
local_port = 80
remote_port = 8000
```
