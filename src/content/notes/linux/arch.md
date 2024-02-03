---
sidebar_position: 1
---

# arch

## install on vps

- wiki: https://gitlab.com/drizzt/vps2arch/-/wikis/Tested-VPS-Providers

- ### ⚠️ 设置 root 的密码

```shell
# wget https://tinyurl.com/vps2arch 也会被重定向到以下 url
wget https://gitlab.com/drizzt/vps2arch/-/raw/master/vps2arch

# 启动脚本
sh ./vps2arch

# 当你从脚本默认的源下载速度较慢的时候，可以使用 -m 参数指定源，例如
sudo sh ./vps2arch -m https://mirrors.neusoft.edu.cn/archlinux/
sync ; reboot -f
```

### 安装

- [archlinux](https://github.com/archlinux/archinstall)
  - install dhcpcd iwd networkmanager
  - systemctl enable --now dhcpcd.service
  - systemctl enable --now iwd.service
  - systemctl enable --now NetworkManager.service

### wifi

```shell
iwctl
device list

station list
station wlan0 scan
station wlan0 show
station wlan0 connect SSID
```

### 源设置

```shell
# /etc/pacman.d/mirrorlist

# 清华大学
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch
# 南京大学
Server = https://mirror.nju.edu.cn/archlinux/$repo/os/$arch
# or
sudo pacman-mirrors -i -c China

sudo pacman -Syy
```

### yay

```shell
git clone https://aur.archlinux.org/yay-bin.git
cd yay-bin
makepkg -si

# pacman -S --needed git base-devel
# git clone https://aur.archlinux.org/yay-bin.git
# cd yay-bin
# makepkg -si
```

### 使用 ntp

```shell
pacman -S ntp
timedatectl set-ntp true
# 设置时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc
```

### utf8

```shell
# 编辑 /etc/locale.gen 取消一下行的注释（你可能需要一个编辑器，如 vim，请自行安装）
en_GB.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8

# 执行 locale-gen

# 创建 /etc/locale.conf 并编辑 LANG 这一 变量，比如：
# LANG=zh_CN.UTF-8
```

### 我的配置

> https://github.com/hjkl01/dotfiles

### 输入法

```shell
sudo pacman -Rs $(pacman -Qsq fcitx)

sudo pacman -S fcitx5 fcitx5-configtool fcitx5-qt fcitx5-gtk fcitx5-chinese-addons

vi ~/.xprofile

export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
fcitx5 &
```

### pppoe 拨号

```shell
yay -S --noconfirm rp-pppoe net-tools

ifconfig # 查看对应的网卡
sudo ifconfig 网卡 down # 停止网卡服务
sudo pppoe-setup # 输入对应的用户名密码等信息
sudo pppoe-start

sudo route delete default
sudo route add default ppp0 # ppp0可能是其他名字 ifconfig查看

sudo nvim /etc/resolvconf.conf # 更新name_servers
sudo resolvconf -u # 更新DNS
```

### missing libcrypto.so.1.1

- https://unix.stackexchange.com/questions/723616/how-to-fix-missing-libcrypto-so-1-1
