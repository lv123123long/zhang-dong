# import
* python程序在import XX时候，是在当前目录，以及安装和第三模块中搜索的，如果搜索不到机会报错
* sys.path.append()可以临时添加搜索路径，方便导入*
## 当前目录
* os.getcwd() 用于获取当前工作目录
* *