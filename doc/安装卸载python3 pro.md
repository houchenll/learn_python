# 安装卸载python3

## mac系统中有哪些python

### 1. mac自带python

通过`which python`或`whereis python`，可以查询到mac自带python命令的位置为：`/usr/bin/python`
与它相伴的命令还有`pydoc`, `pydoc2.7`, `python-config`, `python2.7-config`, `python2`, `python2.7`, `pythonw`, `pythonw2.7`，这9个命令都是软链接，指向`/System/Library/Frameworks/Python.framework/Versions/2.7/bin`中的命令，其中`python`, `python2`, `python2.7`都指向`bin`目录下的`python2.7`，版本为`2.7.16`

### 2. 通过brew安装的python

安装在`/usr/local/Cellar/python@3.9/3.9.6`，并在`/usr/local/bin`中创建软链接

### 3. python安装包包装的python

安装在`/Library/Frameworks/Python.framework/Versions/3.9`，在`/usr/local/bin`下创建软链接：`easy_install-3.9`

### 4. 通过anaconda安装的python

安装在`/Users/ll/opt/anaconda3`

### 5. CommandLineTools

`/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8`，不清楚是什么时候安装的

### 6. 其它python

`/usr/bin/python3`，系统自带命令，删除不了，会自动链接到path或命令行开发工具中的python

## mac系统中有哪些pip

### 1. /usr/bin

`/usr/bin`下有一个`pip3`命令，系统自带命令，只读，删除不了，会自动链接到path或命令行开发工具中的python

### 2. /usr/local/bin

`/usr/local/bin`下有`pip`, `pip3`, `pip3.9`3个命令，是软链接，指向`/usr/local/opt/python@3.9/bin/python3.9`

## 查看

输入`type -a python3`，查看已安装`python3`

```
python3 is /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
python3 is /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
python3 is /usr/local/bin/python3

```

查看已安装`python3`版本: `python3 --version`，输出`Python 3.6.8`

## 卸载python3

```
# folly依赖python，所以卸载python前，先卸载folly
# Uninstalling /usr/local/Cellar/folly/2021.08.23.00... (792 files, 24MB)
brew uninstall folly

# llvm依赖python，所以卸载python前，先卸载llvm
# Uninstalling /usr/local/Cellar/llvm/12.0.1... (9,791 files, 1.6GB)
brew uninstall llvm

# 卸载python 1: brew安装的python
# Uninstalling /usr/local/Cellar/python@3.9/3.9.6... (3,126 files, 55.6MB)
brew uninstall python

# 卸载python 2: command line tools
sudo rm -rf /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework

# 卸载python 3: anaconda3
rm -rf /Users/ll/opt/anaconda3

# 卸载python 4: python官网安装包安装的python
sudo rm -rf /Library/Frameworks/Python.framework

# 卸载python 5: 其它
sudo rm -rf /usr/local/bin/__pycache__
sudo rm -rf /usr/local/bin/easy_install-3.9

# 删除python包
rm -rf /usr/local/lib/python3.9

# 删除pip
sudo rm /usr/local/bin/pip
sudo rm /usr/local/bin/pip3
sudo rm /usr/local/bin/pip3.9

```

执行 `sudo ./uninstall_python3.sh`

> 删除python的环境路径

```
vi ~/.bash_profile

```

> 确认python是否已经删除

```
~ python3
zsh: command not found: python3

```

## 安装

mac系统自带的python是2.7版本，已经过时，现在很多应用都是用的3.x版本，所以需要安装3.x版本。

安装之前，先运行`sudo ./uninstall_python3.sh`，卸载系统原有版本

安装python的方式有很多(homebrew, package, anaconda)，优先使用anaconda方式安装Python

anaconda安装python:
然后按照[官网指导](https://docs.anaconda.com/anaconda/install/mac-os/)，下载`macOS installer`，然后安装

首先排除package安装方式

homebrew安装方式如下：

```
brew install python
# python安装在`/usr/local/Cellar/python@3.9/3.9.7`
# 并在`/usr/local/bin`下创建了以下软链接：pip3.9, wheel3, pip3, python3.9-config, python3.9, python3-config, python3, pydoc3.9, pydoc3, idle3.9, idle3, 2to3-3.9, 2to3
# 并在`/usr/local/opt/`下创建了以下软链接：python, python3, python@3, python@3.9，都指向: /usr/local/Cellar/python@3.9/3.9.7

# 使用以下命令安装python包，包被安装到目录: /usr/local/lib/python3.9/site-packages
pip3 install <package>

# /usr/bin/python3 自动指向了 /usr/local/bin/python3

# 创建软链接
vim ~/.bash_profile
alias python=/usr/local/bin/python3
alias pip=/usr/local/bin/pip3
source ~/.bash_profile

```

## 配置Sublime

启动Sublime Text，并选择菜单ToolsBuild SystemNew Build System，这将打开一 个新的配置文件。删除其中的所有内容，再输入如下内容:

```
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"]
}

```

这些代码让Sublime Text使用命令python3来运行当前打开的文件。请确保其中的路径为你在 前一步使用命令type -a python3获悉的路径。将这个配置文件命名为Python3.sublime-build，并 将其保存到默认目录——你选择菜单Save时Sublime Text打开的目录。
最后使用`command + B`命令，在sublime中运行代码
