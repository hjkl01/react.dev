# 小米刷机

# 小米手机 BL 解锁操作指南

- 备份手机数据，BL 解锁会清除手机数据，有数据的请先外置备份数据
- 手机已插入 SIM 卡，关闭 WiFi 连接，启用数据联网方式（后面操作需要用到数据联网）
- 依次点击 手机设置 -> 我的设备 -> 全部参数 -> 连续点击几次“MIUI 版本” 打开开发者选项（图解）
- 依次点击 手机设置 -> 更多设置 -> 开发者选项 -> 设备解锁状态 -> 绑定帐号和设备（图解）
- 如果首次绑定手机，需要在绑定帐号后等待 7 天，期间不要退出小米帐号，以满足解锁条件（不然后面会提示绑定时间太短）
- 电脑下载小米 BL [解锁工具](https://www.miui.com/unlock/index.html)，完整解压后运行里面的 miflash_unlock.exe 程序，按提示登录小米帐号
- 将手机关机，按住音量下键 + 开机键进入 Fastboot 模式，用数据线连接电脑（如果显示未连接，请检测安装电脑驱动）
- 识别手机连接后，点击“解锁”按钮，稍等片刻就会看到 BL 解锁结果，然后重启手机（开机可看到 BL 锁状态）
- 到此，BL 解锁就完成了，之后可以按需使用线刷方式刷机或者 Root 手机等操作

# 使用命令 adb 和 fastboot 刷机

```shell
# 下载地址: https://get.pixelexperience.org/alioth
# 下载的版本对应设置的安卓版本
# 手机关机后长按 音量下键 + 电源键 进入 FASTBOOT 模式，用数据线连接到电脑。
# 尽量只连接一台设备
fastboot boot PixelExperience_Plus_alioth-13.0-20230119-0804-OFFICIAL.img

# xiaomi k40
# 不要恢复什么东西 不然不能打开Wi-Fi
# fastboot flash boot PixelExperience_Plus_alioth-13.0-20230119-0804-OFFICIAL.img && fastboot reboot-recovery

# 进入 Recovery 后，先清除内部储存和缓存，点击 Factory reset，再点击 Format data / factory reset，点击 format data 确认格式化。
# 然后点击右上角箭头图标返回主界面，点击 Apply update，再点击 Apply from ADB，接着电脑输入命令开始推包刷机。
adb sideload PixelExperience_alioth-12.1-20220920-0632-OFFICIAL.zip
# 刷完后，点击右上角箭头图标返回主界面，点击 Reboot system now，这时就会进入 PixelExperience 系统。
```

# WiFi 提示网络受限

```shell
# 1.  依次点击手机设置 -> 关于手机 -> 连点数次“版本号”启用开发者选项。
# 2.  依次点击手机设置 -> 系统 -> 开发者选项 -> 开启“Android 调试”。
# 3.  手机用数据线连接到电脑，在手机屏幕 USB 调试弹窗允许连接到该电脑。
# 4.  电脑下载 ADB 工具包, 运行命令
adb shell settings put global captive_portal_http_url http://connect.rom.miui.com/generate_204
adb shell settings put global captive_portal_https_url https://connect.rom.miui.com/generate_204
# 5.  运行后断开手机连接，关闭 WiFi 重新打开就解决问题了。
```

# Magisk

```shell
adb push ~/Downloads/PixelExperience_Plus_phoenix-12.1-20220817-1129-OFFICIAL.img /sdcard/Download/boot.img
# 打开Magisk -> 安装 修补 选择并修补 boot.img
adb pull /sdcard/Download/magisk_patched-25200_UCbjh.img .

adb reboot bootloader

fastboot flash boot magisk_patched-25200_UCbjh.img

fastboot reboot
```

<!-- ```shell -->
<!-- adb reboot bootloader -->
<!-- # 再重启进入bootloader -->
<!---->
<!-- fastboot boot PixelExperience_Plus_alioth-13.0-20230119-0804-OFFICIAL.img -->
<!---->
<!-- # Advanced -> Enable ADB -->
<!---->
<!-- adb sideload magisk.zip -->
<!-- 安装完成后，选择 reboot-> system，重启进入系统。恢复备份。 -->

````

# mitmproxy root cert

```shell
# cd ~/.mitmproxy/
openssl x509 -inform PEM -subject_hash_old -in mitmproxy-ca-cert.cer | head -1
cp mitmproxy-ca-cert.cer c8450d0d.0

#传入手机
adb push c8750f0d.0 /sdcard

#获取手机的root权限
adb shell
su

#挂载系统目录为可写
mount -o rw,remount /
mv /sdcard/c8750f0d.0 /system/etc/security/cacerts

#修改证书权限
chmod 644 /system/etc/security/cacerts/c8750f0d.0

# adb reboot
````

# links

- https://wiki.pixelexperience.org/devices/phoenix/install/
- https://get.pixelexperience.org/alioth
- https://miuiver.com/install-pixelexperience-on-xiaomi/
- https://github.com/topjohnwu/Magisk/releases
- https://xiaomishequ.feishu.cn/sheets/shtcnsRTbwSvpUsaei6B04ogI6Z?sheet=bRyHnR
- https://miuiver.com/aosp-rom-of-xiaomi/
