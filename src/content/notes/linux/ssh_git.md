---
sidebar_position: 1
---

# git ssh

### git

```shell
# generate public key
git config --global user.name ""
git config --global user.email ""
ssh-keygen -t rsa -b 4096 -C ""

# git config
git config --global http.https://github.com.proxy socks5://127.0.0.1:7890
git config --global https.https://github.com.proxy socks5://127.0.0.1:7890

# git submodule
git submodule add https://github.com/liuyib/hexo-theme-stun/ themes/stun
git submodule update --remote
```

#### ~/.gitconfig

```shell
# ~/.gitconfig
[pull]
	rebase = false
[user]
	email =
	name =
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[init]
	defaultBranch = master

[alias]
  lg = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
  lp = log --stat -p

; [http "https://github.com"]
; 	postBuffer = 524288000
; 	proxy = socks5://127.0.0.1:1080
; [https "https://github.com"]
; 	postBuffer = 524288000
; 	proxy = socks5://127.0.0.1:1080

; [url "https://gitclone.com/github.com/"]
[url "https://ghproxy.com/https://github.com/"]
	insteadOf = https://github.com
```

#### git commands

```shell
git branch -a # 查看全部分支
git checkout -b dev # 创建并检出一个新的分支
git add somefile
git commit -m "update feature"
git push -u origin dev

git checkout master
git merge dev
git branch -d dev # 删除dev分支
git branch -d origin/dev # 删除远程dev分支

# 回退版本
git reset --hard HEAD^
git reset --hard somecommit
```

### ssh

```shell
# $HOME/.ssh/config

Host archServer
    HostName 192.168.xx.xx
    User xxx
    Port xxx
    # AddressFamily inet # use ipv4
    # AddressFamily inet6 # use ipv6
    IdentitiesOnly yes
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 120
    # DynamicForward localhsot:1080
    # LocalForward localhost:5432 remote-host:5432
    # RemoteForward remote-port target-host:target-port

# 转发跳板机端口
ssh -tt -i ./id_rsa -L 0.0.0.0:local_port:host2:host2_port user@host1

# 上传公钥到目标服务器
ssh-copy-id -i ~/.ssh/id_rsa.pub archServer

# 转发服务器到本机的1082端口
ssh -D 1082 -f -C -q -N archServer

# Host github
#    HostName github.com
#    User git
#    # 走 HTTP 代理
#    # ProxyCommand socat - PROXY:127.0.0.1:%h:%p,proxyport=8080
#    # 走 socks5 代理
#    ProxyCommand nc -v -x 127.0.0.1:7890 %h %p
```

#### ssh TOTP 开启二次验证

```shell
# ubuntu
sudo apt install -y libpam-google-authenticator

# arch
# yay -S --noconfirm google-authenticator-libpam-git
sudo pacman -S --noconfirm libpam-google-authenticator

# 生成验证码
# 哪个账号需要动态验证码，请切换到该账号下操作
# -t: 使用 TOTP 验证
# -f: 将配置保存到 ~/.google_authenticator 文件里面
# -d: 不允许重复使用以前使用的令牌
# -w 3: 使用令牌进行身份验证以进行时钟偏移
# -e 10: 生成 10 个紧急备用代码
# -r 3 -R 30: 限速 - 每 30 秒允许 3 次登录
google-authenticator -t -f -d -w 3 -e 10 -r 3 -R 30

# chrome 插件 https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai
# android app Google Authenticator https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US&gl=US

sudo vim /etc/pam.d/sshd

auth required pam_google_authenticator.so

sudo nvim /etc/ssh/sshd_config

KbdInteractiveAuthentication yes
ChallengeResponseAuthentication yes
PubkeyAuthentication yes
PasswordAuthentication yes
AuthenticationMethods publickey keyboard-interactive
# AuthenticationMethods keyboard-interactive

sudo systemctl restart ssh.service
```

### github

#### 星图

##### 在 markdown 中的代码:

```shell
![stars](https://starchart.cc/lesssound/pornhub.svg)
```

##### example:

![stars](https://starchart.cc/lesssound/pornhub.svg)

#### git 技巧

```shell
git log --after="2020-15-05" --before="2020-25-05"

git log --after="yesterday" // shows only commits from yeserday

git log --after="today" // shows only today commits

git log --before="10 day ago" // omits last 10 days commits

git log --after="1 week ago" //show only commits from last week

git log --after="2 week ago"

git log --after="2 month ago" // shows only last 2 months commits

# git log with diff changes
git log -p

# Filter commits by author
git log --author="Srebalaji"

# Filter commits by log messages
git log --grep="ISSUE-43560"
# To make the search case insensitive, you can pass -i parameter
git log -i --grep="issue-43560"

# Filter commits by files
git log main.rb

# Filter commits by file content
git log -S"function login()"

# Custom formatting log messages
git log --pretty=format:"%Cred%an - %ar%n %Cblue %h -%Cgreen %s %n"
```
