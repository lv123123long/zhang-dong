# 基本概念
## Realm （领域）
*类似于namespace的概念，一个realm包含多个principal。一个principal属于一个特定的realm。*
## Principal(重要的)  princip(原则)
* 认证的主体，可以认为等效于用户名。
* Principal的名称格式为

```
name/role@realm
```
## Keytab
* 二进制文件。包含了principal和加密了的principal密钥信息，可以用来认证principal。
* 
### Kadmin
*Kadmin即Kerberos administration server，运行在主kerberos节点。负责存储KDC数据库，管理principal信息。

## 配置文件krb5.conf



