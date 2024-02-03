# nginx

> 可视化配置 [nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

> 在线配置 [nginxconfig.io](https://digitalocean.github.io/nginxconfig.io/?global.app.lang=zhCN)

## https 证书

```shell
# 安装certbot
# sudo ufw allow 80
yay -S --noconfirm certbot
sudo certbot certonly --standalone -d domain
sudo certbot certonly -d domain --webroot -w /html/filepath/

sudo crontab -e
15 2 * */2 * systemctl stop nginx.service && certbot renew && systemctl restart nginx.service
```

## 基本配置

```shell
server {
    listen 80;
    listen [::]:80;
    server_name blog.hjkl01.cn;

    # 静态文件

    # root /html/github;
    # location / {
    #    index index.html index.htm;
    # }

    root /html/github/;

	  location / {
	  	# try_files $uri $uri/ =404;
	  	try_files $uri $uri /index.html;
	  }


    # ip
    location / {
        default_type application/json;
        return 200 "{\"ip\":\"$remote_addr\"}";
    }


    # django
    location /static/ {
        alias /home/ubuntu/djangoapp/static/;
    }

    location /media/ {
        alias /home/ubuntu/djangoapp/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
        add_header P3P 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
        add_header Access-Control-Allow-Origin *;
    }


    # 转发端口
    location / {
        proxy_pass http://127.0.0.1:8000/;
    }

    # 重定向
    return 301 https://$host$request_uri;
    # rewrite ^(.*)$ https://blog.hjkl01.cn; #将所有HTTP请求通过rewrite指令重定向到HTTPS。

    # CORS
    add_header Access-Control-Allow-Origin *;
    add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
    add_header Access-Control-Allow-Headers 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization';

}
```

### ssl

```shell
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name blog.hjkl01.cn;

    ssl_certificate /etc/letsencrypt/live/blog.hjkl01.cn/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/blog.hjkl01.cn/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/blog.hjkl01.cn/chain.pem;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    # 静态文件
    location / {
        root /html/github;  #站点目录。
        index index.html index.htm;
    }

    # 转发端口
    location / {
        proxy_pass http://127.0.0.1:8080/;
    }

}
```

### 转发 mongo 端口(TCP)

```shell
stream {
    server {
        listen  <your incoming Mongo TCP port>;
        proxy_connect_timeout 1s;
        proxy_timeout 3s;
        proxy_pass    stream_mongo_backend;
    }

    upstream stream_mongo_backend {
      server <localhost:your local Mongo TCP port>;
  }
}
```

## 限流

### 正常限流

```shell
# nginx.conf
http {
    limit_req_zone $binary_remote_addr zone=myRateLimit:10m rate=10r/s;
}
# server
server {
        location / {
            limit_req zone=myRateLimit;
            proxy_pass http://my_upstream;
        }
}
```

- key ：定义限流对象，binary*remote_addr 是一种 key，表示基于 remote_addr(客户端 IP) 来做限流，binary* 的目的是压缩内存占用量。
- zone：定义共享内存区来存储访问信息， myRateLimit:10m 表示一个大小为 10M，名字为 myRateLimit 的内存区域。1M 能存储 16000 IP 地址的访问信息，10M 可以存储 16W IP 地址访问信息。
- rate 用于设置最大访问速率，rate=10r/s 表示每秒最多处理 10 个请求。Nginx 实际上以毫秒为粒度来跟踪请求信息，因此 10r/s 实际上是限制：每 100 毫秒处理一个请求。这意味着，自上一个请求处理完后，若后续 100 毫秒内又有请求到达，将拒绝处理该请求。

### 处理突发流量

```shell
server {
        location / {
            limit_req zone=myRateLimit burst=20 nodelay;
            proxy_pass http://my_upstream;
        }
    }
```

### 限制连接数

```shell
limit_conn_zone $binary_remote_addr zone=perip:10m;
limit_conn_zone $server_name zone=perserver:10m;
server {
    ...
    limit_conn perip 10;
    limit_conn perserver 100;
}
```

- limit_conn perip 10 作用的 key 是 $binary_remote_addr，表示限制单个 IP 同时最多能持有 10 个连接。

- limit_conn perserver 100 作用的 key 是 $server_name，表示虚拟主机(server) 同时能处理并发连接的总数。

- 需要注意的是：只有当 request header 被后端 server 处理后，这个连接才进行计数。

### 设置白名单

```shell
# nginx.conf
geo $limit {
    default 1;
    10.0.0.0/8 0;
    192.168.0.0/24 0;
    172.20.0.35 0;
}
map $limit $limit_key {
    0 "";
    1 $binary_remote_addr;
}
limit_req_zone $limit_key zone=myRateLimit:10m rate=10r/s;
```

- geo 对于白名单(子网或 IP 都可以) 将返回 0，其他 IP 将返回 1。

- map 将 $limit 转换为 $limit_key，如果是 $limit 是 0(白名单)，则返回空字符串；如果是 1，则返回客户端实际 IP。

- limit_req_zone 限流的 key 不再使用 $binary_remote_addr，而是 $limit_key 来动态获取值。如果是白名单，limit_req_zone 的限流 key 则为空字符串，将不会限流；若不是白名单，将会对客户端真实 IP 进行限流。

### 限制数据传输速度

```shell
location /flv/ {
    flv;
    limit_rate_after 20m;
    limit_rate       100k;
}
```

- 这个限制是针对每个请求的，表示客户端下载前 20M 时不限速，后续限制 100kb/s。

## goaccess

```shell
# /etc/goaccess/goaccess.conf

log-format %h %^[%d:%t %^] "%r" %s %b "%R" "%u"
date-format %d/%b/%Y
time-format %H:%M:%S
output /usr/share/nginx/html/index.html

# crontab
*/30 * * * * goaccess -a -d -f /var/log/nginx/access.log -p /etc/goaccess/goaccess.conf

# 可以设置LANG为zh_CN 界面会变为中文
```
