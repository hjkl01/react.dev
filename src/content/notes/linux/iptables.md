# iptables

```shell
# 查看
sudo ip6tables -vnL

# example config
*filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -i lo -j ACCEPT

-A INPUT -p tcp --dport 22 -j ACCEPT
-A INPUT -p tcp --dport 10000:20000 -j ACCEPT
COMMIT
```
