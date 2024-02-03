---
sidebar_position: 1
---

# Mac

## brew

### 安装

```shell
# 安装
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"

# 从清华镜像下载安装脚本并安装 Homebrew / Linuxbrew
export HOMEBREW_API_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/api

git clone --depth=1 https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/install.git brew-install
/bin/bash brew-install/install.sh
rm -rf brew-install

# 也可从 GitHub 获取官方安装脚本安装 Homebrew / Linuxbrew
/bin/bash -c "$(curl -fsSL https://github.com/Homebrew/install/raw/master/install.sh)"

```

```shell
# software
iredis
pgcli
mycli
scrcpy
viu
proxychains-ng


# open chrome with proxy
open -a /Applications/Google\ Chrome.app/ --args --proxy-server=127.0.0.1:7890
```

## brew cask

### shell

> iterm2
> alacritty](https://github.com/alacritty/alacritty/releases)
> tmux

### 视频播放器

> iina

### sql 可视化管理

> tableplus

### vnc 客户端, 比 Mac 自带的流畅

> vnc-viewer

### 字体

> font-fira-code font-fira-code-nerd-font

```shell
brew tap homebrew/cask-fonts
brew install --cask font-fira-code
brew install font-fira-mono-nerd-font
```

### 控制电池充电量

> aldente

### 窗口管理

> rectangle

```shell
brew install --cask rectangle
```

### 平滑鼠标滚动

> mos

### Mac 终端录屏

> ttygif

```shell
# https://github.com/icholy/ttygif
brew install ttygif
ttyrec myrecording
# On OSX optionally you can set a -f flag which will bypass cropping which is needed for terminal apps which aren't full screen. Both standard Terminal and iTerm apps are supported.
ttygif myrecording -f
```

### 在 touch bar 上显示歌词

> [LyricsX](https://github.com/ddddxxx/LyricsX)
