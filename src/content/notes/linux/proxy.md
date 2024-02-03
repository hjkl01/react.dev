# proxy

## clash yacd

```yaml
version: "3.8"

services:
  yacd:
    container_name: yacd
    image: haishanh/yacd
    ports:
      - 127.0.0.1:1234:80
    restart: unless-stopped
```

## [glider](https://github.com/nadoo/glider/blob/master/config/glider.conf.example)

```shell
yay -S glider

glider -listen :1080 -forward trojan://password@ip:443

# with auth
glider -listen user:user_passwd@:61000 -forward trojan://password@ip:443

# or glider.conf
listen=:1080
# with user and password
listen=user:passwd@:1080
forward=trojan://password@ip:443
```

## clash config to glider

```python
# pip install pyyaml
import yaml

filename = "./config.yaml"
with open(filename, "r") as file:
    con = yaml.safe_load(file)

for server in con["proxies"]:
    res = f"forward=trojan://{server['password']}@{server['server']}:{server['port']}"
    print(res)
```

## trojan/trojan-go

```shell
https://github.com/trojan-gfw/trojan

# 机场推荐: https://portal.shadowsocks.nz/aff.php?aff=24252

# 部署参考 https://github.com/Jrohy/trojan

ufw allow 80 443 8443
# 生成证书
certbot certonly --standalone -d domain.com -v
# crontab
15 2 * */2 * certbot renew

# arch 开启 bbr
echo "tcp_bbr" > /etc/modules-load.d/modules.conf

echo "net.core.default_qdisc=fq" > /etc/sysctl.d/bbr.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.d/bbr.conf
reboot

# 验证
sysctl net.ipv4.tcp_congestion_control
# net.ipv4.tcp_congestion_control = bbr
```

### server /etc/trojan/config.json

<!-- - https://trojan-gfw.github.io/trojan/config -->

- https://github.com/p4gefau1t/trojan-go/releases

```json
{
  "run_type": "server",
  "local_addr": "0.0.0.0",
  "local_port": 8443,
  "remote_addr": "github.com",
  "remote_port": 80,
  "password": ["domain.com"],
  "ssl": {
    "cert": "/var/lib/caddy/certificates/acme-v02.api.letsencrypt.org-directory/domain.com/domain.com.crt",
    "key": "/var/lib/caddy/certificates/acme-v02.api.letsencrypt.org-directory/domain.com/domain.com.key",
    "sni": "domain.com"
  }
}
```

### client config.json

```json
{
  "run_type": "client",
  "local_addr": "127.0.0.1",
  "local_port": 1080,
  "remote_addr": "domain.com",
  "remote_port": 8443,
  "password": ["domain.com"],
  "ssl": {
    "sni": "domain.com"
  },
  "mux": {
    "enabled": true
  }
}
```

## socks5 转 http

## privoxy 配置

```shell
yay -S privoxy

cd /etc/privoxy

(sudo) mv config config.bak
(sudo) vi config

forward-socks5t / 127.0.0.1:1080 .
listen-address 127.0.0.1:9888

sudo systemctl restart privoxy.service
sudo systemctl enable privoxy.service
```

# 旧

## server:

```shell
install libsodium
pip install shadowsocks
pip install https://github.com/shadowsocks/shadowsocks/archive/master.zip -U

# path : /etc/shadowsocks.json
{
    "server":"0.0.0.0",
    "port_password": {
        "8000": "password"
    },
    "timeout":300,
    "method":"chacha20-ietf-poly1305",
    "fast_open":true,
    "pid-file": "/path/ss.pid",
    "log-file": "/path/ss.log"
}

(sudo) ssserver -c /etc/shadowsocks.json -d start
sudo ssserver -d stop

https://github.com/shadowsocks/shadowsocks/wiki/Shadowsocks-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E
```

#### 开启 bbr

```shell
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh

chmod +x bbr.sh

./bbr.sh

sysctl net.ipv4.tcp_available_congestion_control
#返回值一般为：
#net.ipv4.tcp_available_congestion_control = bbr cubic reno

sysctl net.ipv4.tcp_congestion_control
#返回值一般为：
#net.ipv4.tcp_congestion_control = bbr

sysctl net.core.default_qdisc
#返回值一般为：
#net.core.default_qdisc = fq

lsmod | grep bbr
#返回值有 tcp_bbr 模块即说明bbr已启动。
```

## client

#### ubuntu 下使用， Mac 下载 https://github.com/shadowsocks/ShadowsocksX-NG/releases/

```shell
pip install shadowsocks

path : ~/.shadowsocks/shadowsocks.json

{
  "server":"my_server_ip",
  "server_port":my_server_port,
  "password":"my_password",
  "local_address": "127.0.0.1",
  "local_port":1080,
  "timeout":300,
  "method":"chacha20-ietf-poly1305",
  "fast_open":true,
  "pid-file": "/path",
  "log-file": "/path"
}

sslocal -c ~/.shadowsocks/shadowsocks.json -d start
可先在系统设置里设置全局代理，在浏览器里安装 https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif
```
