## fileglob
* fileglob查询的只能是本地端的文件
* 
```
tasks: 
    - name: task1
      debug:
        msg: "filenames: {{lookup('fileglob','/etc/*.conf')}}"
```
* 
## file
* 可以查询目标主机的信息
* *
```
tasks: 
    - name: task1
      debug:
        msg: "file content: {{lookup('file','/etc/hosts')}}"

```
## pipe
* 从ansible端的一个命令执行结果中读取数据
* 
```
tasks: 
    - name: task1
      debug:
        msg: "command res: {{lookup('pipe','cat /etc/hosts')}}"

```


# 返回的结果
* lookup()查询出来的结果包含多项，默认是以逗号分隔各项的字符串返回
* 可以给lookup传递一个参数，wantlist=True  返回的结果就是以**列表**的方式


## 新特性
* 在Ansible 2.5中添加了一个新的功能query()或q()，后者是前者的等价缩写形式。query()在写法和功能上和lookup一致，其实它会自动调用lookup插件，并且总是以列表方式返回，而不需要手动加上wantlist=True参数
```
- name: task1
  debug:
    msg: "{{q('fileglob','/etc/*.conf')}}"

```
## vars 设置变量
* vasr可以设置在play级别，也可以设置在taskjibie
* play级别，所有task都可以访问
* task级别，只有该task可以访问
## when 条件判断
* ansible作为一个编排、协调的配置管理工具
* 提供了流程控制，比如条件判断，循环，退出等
* true为执行，否则不执行跳过
*
