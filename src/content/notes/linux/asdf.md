# asdf

### install asdf

```shell
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.0

# add following to ~/.zshrc
# mac
# . /usr/local/opt/asdf/libexec/asdf.sh

# linux
. $HOME/.asdf/asdf.sh
```

### install plugin example

```shell
asdf plugin add nodejs
asdf list all nodejs
asdf install nodejs lts
# asdf install nodejs latest
asdf list nodejs
asdf global nodejs lts
```
