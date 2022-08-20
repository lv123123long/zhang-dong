* 一般放在项目的根目录下
# 结构及参数
```
[pytest] 
addopts = -v -s --html=py_test/scripts/report/report.html -p no:warnings --reruns=1 ，配置运行时的参数 
testpaths = ./py_test/scripts，配置要跑的脚本在哪个目录下
```
```
python_files= test_rerun.py，配置测试文件匹配模式 
python_classes = Test*，配置测试类的匹配模式，比如这个是类文件以Test开头，则可以匹配到 python_function = test*，配置函数 、方法匹配模式，比如这个是以test开头则可以匹配到 xfail_strict = true，配置是否允许预期失败的用例存在
```
* 不希望出现预取失败结果成功的情况，添加配置项
* xfail_strict = true
* 