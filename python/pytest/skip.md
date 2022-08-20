# pytest.skip
* 用于函数内，跳过测试用例
```
def test_2():

    if 1 < 2:

        pytest.skip('1111111')

    pass
```
* @pytest.mark.skip(用于函数外，跳过测试用例)
```
@pytest.mark.skip(reason='feature not implemented')

def test_1():

    pass

# 模块级别跳过。（注：参数allow_module_level的值设为True）

pytest.skip('skip all tests', allow_module_level=True)
```
* @pytest.mark.skipif(用于函数外，条件是condition，跳过原因是reason='xxx')*
```
@pytest.mark.skipif(condition='1<2',reason='feature not implemented')
def test_1():
	pass
```
## ordering-执行顺序
* 控制用例执行顺序的方法
* 在需要调整用例执行顺序的函数或者方法前增加
* @pytest.mark.run(order=x)
1. x表示数字形式：小数，整数，负数
2. 由小到大
3. 由正到负
4. 未标记的在正数后，负数前执行
5. 顺序： 1，2，3，无标记，-3，-2，-4
## xfail 预期失败
* xfail（condition,reason）*
* condition 预期失败的条件
* reason预期失败的原因
* xfail-strict=true，则只需要被pytest.mark.xfail标记的方法，结果都为失败：若xfail-strict=false，则被pytest.mark.xfail标记的方法，按照实际执行情况来看是否成功或失败
## 失败重跑
安装pytest-rerunfailure  
在设置文件pytest.ini中添加命令  
reruns = 重跑次数  
addopts = --reruns=10
