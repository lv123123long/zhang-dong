# kerberos基本原理
## keberos是什么
* MIT（麻省理工大学）提出的**网络身份验证协议**，旨在通过使用**密钥加密技术**为客户端和服务器应用程序提供强身份验证
* kerberos是一种基于Ticket的身份认证协议，由三部分组成
1. KDC   (Key Distribution center)
2. Client
3. Service
* 客户端会先访问两次KDC，再去访问目标服务
1. Authentication Server  (认证)
2. Ticket Granting Server  (票据授予)
## 基本概念
### Principle
Principle可以认为是kerberos的用户名，用于标识身份，principle由三部分组成
1. primary(#基本的)
2. instance(可选)（#实例）
3. realm
* 包含instance的一般为server的principle     hiveserver2/foc.alibaba.com@EXAM.COM    ----------primary/instance@realm
* 不包含instance，一般是客户端的principle，用于身份认证*     xioaming@EXAM.COM  ----------primary@raelm
### keytab
* 相当于密码本，包含了多个principle与密码的文件，用户可以利用该文件进行身份认证
### Ticket Cache
* 客户端与KDC交互完后，包含身份认证信息的文件，短期有效，需要不断renew
### Realm
* 不同kerberos的区分，，属于kerberos的一个namespace
### KDC
由三部分组成
1. kerberos database ：包含了一个realm中的所有的principle、密码与其他信息；默认是Berkeley DB
2. Authentication Setver(AS)：进行用户信息认证的，为客户端提供TGT（Ticket Granting Tickets）
3. Ticket Granting Server(TGS)：验证TGT与Authenticator，为客户端提供Service Tickets
## 基本工作原理
1. 客户端与AS或TGS都会获取到两条信息，其中一条可以解密，另外一条无法解密
2. 客户端想要访问目标服务不会直接与KDC交互
3. KDC Database包含所有客户端与服务的密码
4. 密钥都是密码加salt后经过哈希处理得到的。密钥都是由管理员生成的，并分发到客户端和服务
5. KDC本身使用主密钥进行加密，以增进从数据库中窃取密钥的难度
6. kerberos中信息加密的方式一般是对称加密，也可以是非对称加密
### kerberos的优势
* 密码不需要网络传输；基于Ticket实现身份认证，保证密钥安全性
* 双向认证，整个认证过程中，不仅客户端需要认证，待访问的服务也需要进行身份认证
* 高性能；一旦客户端获取到了服务所需的Ticket，该Service就能根据这个Ticket实现对客户端的验证，不再需要KDC的再次参与*


**数据库运行在server上面**
kdc运行在kdc机器上面