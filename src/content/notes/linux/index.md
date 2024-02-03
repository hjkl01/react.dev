---
sidebar_position: 0
---

# index

## 我的配置文件

- https://github.com/hjkl01/dotfiles

## zsh

```
# run command background
1. setopt NO_HUP
2. nohup <command> & disown
```

## find

```shell
# find by name
find . -name "*.log"
grep "hello" example.txt
grep -r "hello" my_directory

# udpate filename
find . -type f -name 'some.*' | while read FILE; do
    newfile="$(echo ${FILE} | sed -e 's/some/result/')"
    mv "${FILE}" "${newfile}"
done

# delte size < 1k
find -size 1k -delete

# 从根目录开始查找所有扩展名为 .log 的文本文件，并找出包含 "ERROR" 的行：
find / -type f -name "*.log" | xargs grep "ERROR"

# 从当前目录开始查找所有扩展名为 .in 的文本文件，并找出包含 "thermcontact" 的行：
find . -name "*.in" | xargs grep "thermcontact"
```
