# Server
## 安装
* krb5-server*
## 配置
### /etc/krb5.conf
* 需要配置realm领域名称
* kdc 运行机器
* admin_server 机器*
### /var/kerberos/krb5kdc/kdc.conf
* kdc端口号
* realm数据库配置
* 加密的密钥类型
* acl文件，，用于指定哪些用户可以访问kdc数据库的控制文件
* admin_keytab：KDC进行校验的的keytab
### /var/kerberos/krb5kdc/kadm5.acl
* kerberos kadmind使用该文件来管理对kerberos数据库的访问权限，对于影响principal的操作，ACL文件还可以控制哪些principal可以对哪些其他principal进行操作
*\ */admin@ABC.COM *
* 文件格式解析：principal  permissions  [target_principal  [restrictions] ]
* principal：设置该 principal 的权限；principal 的每个部分都可以使用 *。
* permissions： 权限，有如下一些权限：
* target_principal：目标 principal，目标 principal 的每个部分都可以使用 *。
* restrictions(限制)：针对权限的一些补充限制，如：限制创建的 principal 的票据最长时效。
* ACL 文件中的行顺序很重要，会使用第一个匹配的行来设置用户权限。

## kadmin.local
* 来进行各种管理操作*


# Client
### 安装
* krb5-workstation
* 把服务器的/etc/krb5.conf复制过来覆盖本地的/etc/krb5.conf
### kadmin
* kerberos可以用kadmin来执行各种管理的操作。**需要事先在server上创建登录的principal,默认是{当前用户}/admin@realm**
* 就是需要了当前用户可以登录的principal，客户端才能进行操作
### kinit
* 在客户端认证用户
### klist
* 查看当前的认证用户
### kdestroy
* 删掉当前的认证缓存*

