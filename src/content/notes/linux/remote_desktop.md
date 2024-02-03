# remote desktop

## vnc

### 服务端安装

```shell
# ubuntu
  sudo apt-get install x11vnc

  x11vnc -storepasswd

  x11vnc -auth guess -once -loop -noxdamage -repeat -rfbauth ~/.vnc/passwd -rfbport 5900 -shared

  x11vnc -forever

  https://www.realvnc.com/en/connect/download/viewer/


# arch

## old
  yay -S x11vnc net-tools
  update -> /etc/gdm/custom.conf:
      WaylandEnable=false

  x11vnc -wait 50 -noxdamage -passwd PASSWORD -display :0 -forever -o /var/log/x11vnc.log -bg

## tigervnc
# 要在 Arch Linux 上启动 VNC，您需要安装一个 VNC 服务器，例如 TigerVNC 或 TightVNC。然后，您可以使用以下步骤启动 VNC：

# 1. 安装 VNC 服务器：
sudo pacman -S tigervnc

# 2. 设置 VNC 密码：
vncpasswd

# 3. 启动 VNC 服务器：
vncserver :1
这将启动一个名为“:1”的 VNC 服务器实例。如果您需要启动多个实例，可以使用“:2”、“:3”等等。

# 4. 启动 X11 会话：
startx
这将启动 X11 会话，您可以在其中运行应用程序。

# 5. 启动 VNC 显示器：
x0vncserver -display :1 -passwordfile ~/.vnc/passwd
# 这将启动一个 VNC 显示器，它将连接到您在第 3 步中启动的 VNC 服务器实例。

# 现在，您可以使用 VNC 客户端连接到您的 Arch Linux 系统并远程访问 X11 会话。

```

### 客户端

> https://www.realvnc.com/

```shell
# mac
brew install vnc-viewer


# 错误
# display_server_not_supported

# /etc/gdm3/custom.conf
[daemon]
    # Enabling automatic login
    AutomaticLoginEnable=true
    AutomaticLogin=$USERNAME
    
sudo systemctl restart gdm.service
```

## arch install todesk

```sh
wget https://dl.todesk.com/linux/todesk_2.0.2_x86_64.pkg.tar.zst

sudo pacman -U todesk_2.0.2_x86_64.pkg.tar.zst

sudo systemctl restart todeskd.service
```

### 详情参考

> https://www.todesk.com/download_detail.html
````

