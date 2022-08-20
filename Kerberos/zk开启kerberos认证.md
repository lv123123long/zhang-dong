# kerberos认证
* kerberos认证主要用于客户端与Zookeeper服务端的相互认证
## 认证过程
### 创建keytab
* 在安装kerberos的机器上进入kadmin（客户端用kadmin，服务端用kadmin.local）
* 执行以下命令创建keytab
1. add_principal -randkey zk-server/pxc2@ABC.COM   # pxc2 为zk的主机名
2. add_principal -randkey zk-client@ABC.COM 
3. xst -k /root/zk-server.keytab zk-server/pxc2@ABC.COM 
4. xst -k /root/zk-client.keytab zk-client@ABC.COM 
## 配置
* 复制krb5.conf 及 keytab文件到安装zk的机器上，放到zk的conf目录下，修改zoo.cfg文件
```
authProvider.1=org.apache.zookeeper.server.auth.SASLAuthenticationProvider
jaasLoginRenew=3600000
sessionRequireClientSASLAuth=true #客户端必须 SASL 认证
```
### 新建jaas.conf文件
* 该文件也放到zk的conf目录下
```
Server {
   com.sun.security.auth.module.Krb5LoginModule required
   useKeyTab=true
   keyTab="/home/hadoop/app/apache-zookeeper-3.6.3-bin/conf/zk-server.keytab"
   storeKey=true
   useTicketCache=false
   principal="zk-server/pxc2@ABC.COM";
};

#客户端配置，方便 zkCli.sh 使用
Client {
   com.sun.security.auth.module.Krb5LoginModule required
   useKeyTab=true
   keyTab="/home/hadoop/app/apache-zookeeper-3.6.3-bin/conf/zk-client.keytab"
   storeKey=true
   useTicketCache=false
   principal="zk-client@ABC.COM";
};

```
### 新建java.env文件
* 用于指定jaas文件的位置，也放到zk的conf目录下*
