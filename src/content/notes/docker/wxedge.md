# wxedge

## host 模式

```yaml
docker run -d --name=wxedge --restart=always --privileged --net=host -v /dockers/data:/storage:rw  registry.hub.docker.com/onething1/wxedge
```

## 混杂模式实例

```yaml
sudo ip link set wlp2s0 promisc on
docker network create -d macvlan --subnet=192.168.32.0/24 --gateway=192.168.32.1 -o parent=wlp2s0 macvlandocker
docker run -d --name=wxedge --restart=always --privileged --net=macvlandocker --ip=192.168.32.46 -p 192.168.32.46:18888:18888 -v /dockers/data:/storage:rw  registry.hub.docker.com/onething1/wxedge
```

## 绑定

- 打开 ip:18888, APP 扫码
