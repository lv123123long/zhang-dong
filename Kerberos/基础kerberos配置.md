# 基础kerberos配置
## /etc/krb5.conf
	kerberos的主要配置
## kdc.conf
	kdc的主要配置
## acl_file
* 用于指定哪些用户可以访问kdc数据库的控制文件*
## kadm5.acl
* kerberos kadmind 使用该文件来管理kerberos数据库的访问权限，对于影响principal的操作，ACL文件还控制哪些principal可以对其他principal进行操作
* **ACL文件的行顺序很重要，会使用第一个匹配的行来设置用户权限
### 相关参数说明
* principal：设置该principal的权限，principal的每个部分都可以使用*
* permission：权限，，，，（很多，待定）
## 创建kerberos数据库
```
kdb5_util create -s -r ABC.COM
```
* -s ：表示生成stash file ，并存储在master server key (krb5kdc)
* -r ：指定realm name
## 启动kerberos服务
```
systemctl start krb5kdc
systemctl start kadmin
```
## 停止kerberos服务
```
systemctl stop krb5kdc
systemctl stop kadmin

```

## kerberos的终端--kadmin.local
* kerberos服务器上可以用kadmin.local来执行各种管理的操作
* *
#### 常规操作
  | 操纵 | 描述 | 例子 |
  | add_principal, addprinc, ank |  增加principal |   add_principal -rnadkey  test@ABC.COM |
  | delete_principal, delprinc  | 删掉principal  | delete_principal test@ABC.COM |
  | modify_principal, modprinc |  修改principal | modify_principal test@ABC.COM |
  | rename_principal, renprinc |  重命名principal | rename_principal test@ABC.COM test2@ABC.COM |
  | get_principal, getprinc | 获取principal | get_principal test@ABC.COM |
  | list_principals, listprincs, get_principals, getprincis | 显示所有Principal | listprincs |
  | ktadd, xst | 导出条目到keytab | xst -k /root/test.keytab  test@ABC.COM |
  
  
  
