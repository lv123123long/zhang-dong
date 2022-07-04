# 常用操作
## 初始化
```
kinit -kt /home/用户的.keytab文件 用户@HADOOP.COM

```
## 查询kerberos
```
klist
```
## 用户权限问题
* 不同用户下给的权限不一样，比如在root下给的kerberos认证，切换到work用户就失效了，work用户需要自己的认证*