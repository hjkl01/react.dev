---
sidebar_position: 1
---

# Windows

## ISO

- download tool: https://github.com/agalwood/Motrix/releases

- magnet

  | name       | version           | time       | magnet                                                                  | md5                              |
  | ---------- | ----------------- | ---------- | ----------------------------------------------------------------------- | -------------------------------- |
  | Windows 10 | business editions | 2023-01-17 | [address](magnet:?xt=urn:btih:bd9d2e331935882a56e34eb12dca95f2f8792186) | F108751F073BB69BDC8AE01EED568112 |
  | Windows 10 | consumer editions | 2023-01-17 | [address](magnet:?xt=urn:btih:f3e4fd207d7844f608faebb98db54ddacd414aa3) | F7F102E2F2E35644486F6666A718C1A7 |
  | Windows 11 | business editions | 2023-01-17 | [address](magnet:?xt=urn:btih:01f5fe67f19cf107330490f658836c6037054f65) | F92D309E1DEB81A2FA7A521257250FDA |
  | Windows 11 | consumer editions | 2023-01-17 | [address](magnet:?xt=urn:btih:6fe66b53ece28fa473bf16fbc4c3e0aae2ed36c1) | 59a06042f6abb7910cf5c06480b6d3ab |

## 激活

```shell
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
slmgr /skms kms.03k.org
slmgr /ato
```

## 开机启动文件夹 start

- win+R shell:Common Startup
- C：\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp

## 开机启动 退出CMD窗口

```
@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
REM

cmd
```

## 更改程序默认按照路径

- 设置 系统 存储 更新内容的保存位置

## 更改录屏保存位置

- 视频 属性 移动

## [ssh server](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell)
