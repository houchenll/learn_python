Anaconda 和 Jupyter（包括Jupyter Notebook和JupyterLab，其中JupyterLab是从Notebook发展而来的）已成为数据分析的标准环境。

简单来说，Anaconda是包管理器和环境管理器，Jupyter可以将数据分析的代码、图像和文档全部组合到一个web文档中。

Anaconda拥有个人版、商业版、团队版、企业版，除个人版不收费外，其他版本都需要付费。

使用Anaconda可以研究数据处理、数据建模、机器学习、神经网络、自然语言处理、可视化展示、教学等等

## 为什么需要 Anaconda

我已经安装了python，为什么还需要Anaconda

1. Anaconda 附带了一大批数据科学包，它附带了 conda、Python 和 150 多个科学包及其依赖项。因此可以立即处理数据。
2. 管理包：
Anaconda 是在 conda (一个包管理器和环境管理器) 上发展出来的。
在数据分析中，会用到很多第三方的包，而 conda 可以很好的帮助你在计算机上安装和管理这些包，包括安装、卸载和更新包。
3. 管理环境：
为什么要管理环境？
比如你在A项目用了 Python2，而新的项目B需要使用 Python3，而同时安装两个 Python 版本可能会造成许多混乱和错误。这时候 conda 可以帮助你为不同的项目建立不同的运行环境。
还有很多项目使用的包版本不同，比如不同的 pandas 版本，不可能同时安装两个 numpy 版本，你要做的应该是，为每个 numpy 版本创建一个环境，然后项目在对应环境中工作。这些 conda 可以帮助你做到。

## conda

Conda是一个开源、跨平台和语言无关的软件包管理和系统管理系统，通过Conda可安装、升级和升级软件包依赖。
conda和pip都可以管理python库，但最大的不同在于conda是跨平台且不限语言的，而且可以独自创建虚拟环境。因为conda立足于数据科学生态，不像pip可以安装几乎所有的ptyhon库(来自pypl)，conda只能安装anaconda里支持的数据科学库(600多个)。
主要的数据科学内置库包括：pandas, numpy, matplotlib, jupyter, scipy, ipython, nltk, notebook, sikit-learn, seaborn, xlrd, xlwt, ...
一般把这些数据科学库分为四大类：基础库(jupyter, pandas, numpy, scipy)、机器学习库(keras, tensorflow, pytorch, sikit-learn, nltk)、可视化库(matplotlib, seaborn, plotly)、拓展计算库(numba, dask, pyspark)
这些库可以通过conda安装，也可以在GUI界面Navigaor上点击安装或更新
这里可看查看[Anaconda package lists](https://docs.anaconda.com/anaconda/packages/pkg-docs/)[conda文档](https://docs.conda.io/en/latest/)

## 怎么安装 Anaconda

先卸载已安装的python
然后按照[官网指导](https://docs.anaconda.com/anaconda/install/mac-os/)，下载`macOS installer`，然后安装。
安装程序把anaconda安装在 `/opt/anaconda3`，其bin目录下有 `conda`, `jupyter`, `python`, `pip`等很多命令
安装程序会自动修改 `.bash_profile`，在尾部添加 `conda` 初始化代码，把 `/opt/anaconda3/bin` 添加到 `PATH`
并把`python`命令指向`/opt/anaconda3/bin/python`, `pip`指向`/opt/anaconda3/bin/pip`

安装成功后，默认环境为base(root)，其下默认有354个包，包括`numpy`, `pandas`, `python`
创建的新环境位于`/opt/anaconda3/envs`下，默认有15个包

查看[Getting Started with Anaconda Individual Edition](https://anaconda.cloud/tutorials/getting-started-with-anaconda-individual-edition?source=osx_installer)或[User Guide](https://docs.anaconda.com/anaconda/user-guide/?utm_source=anaconda.com&utm_medium=individual-get-started) 以了解更多

## miniconda

Anaconda的优点也是它的缺点，功能太齐全就显得臃肿，一个安装包快500M，所以不少人去拥抱miniconda了。

## 使用 Anaconda Navigaor 管理包

通过应用列表，打开 Anaconda Navigator，选择 Environments -> root -> Installed，查看各个环境中已安装的包
点击不同的环境名，可以切换环境
点击包名左边的勾选框，选择版本，点击aplly，以更新版本

## 常用命令

anaconda-navigator: 打开 Anaconda Navigator
conda install <package>
