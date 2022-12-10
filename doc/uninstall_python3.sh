# brew
brew uninstall folly
brew uninstall llvm
brew uninstall python
# package
sudo rm -rf /Library/Frameworks/Python.framework
sudo rm -rf /Applications/Python*
# command line tool
sudo rm -rf /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework
# anaconda
rm -rf ~/opt/anaconda3
rm -rf ~/env/miniconda3
rm -rf ~/.anaconda
rm -rf ~/.conda
rm ~/.condarc
rm -rf ~/.jupyter
# /usr/local/bin
sudo rm -rf /usr/local/bin/__pycache__
sudo rm -rf /usr/local/bin/easy_install*
sudo rm -rf /usr/local/bin/2to3*
sudo rm -rf /usr/local/bin/idle3*
sudo rm -rf /usr/local/bin/pip3*
sudo rm -rf /usr/local/bin/pydoc3*
sudo rm -rf /usr/local/bin/python3*
# 删除python包
rm -rf /usr/local/lib/python3.9
# pip
sudo rm /usr/local/bin/pip
sudo rm /usr/local/bin/pip3
sudo rm /usr/local/bin/pip3.9
# other
rm -rf ~/.ipython
rm ~/.python_history
rm -rf ~/.tender
sudo rm -rf ~/.virtualenvs
