# 概念
| **DC** | 域控 | | **KDC** | 密钥分发中心，域控担任 | | **AD** | 活动目录，包含与用户数据库 | | **AS** | Kerberos认证服务 | | **TGT** | AS分发，TGT认证权证 | | **TGS** | 票据授予服务 | | **ST** | ST服务票据，由TGS服务发送 |


![[Pasted image 20220630182047.png]]

* krbtgt用户，是系统在创建域时自动生成的一个帐号，其作用是密钥分发中心的服务账号，其密码是系统随机生成的，无法登录主机

**Kerberos 是一种由 MIT(麻省理工大学)提出的网络身份验证协议，它旨在通过使用密钥加密技术为客户端和服务器应用程序提供强身份验证**
* Kerberos 是一种基于加密 Ticket 的身份认证协议，主要由三个部分组成：Key Distribution Center (即KDC)、Client 和 Service*
* 客户端会先访问两次 KDC，然后再访问目标服务，如：HTTP 服务、Zookeeper 服务、Kafka 服务等。
* 
# kerberos基本概念
## 2.1 Principal
* Principal 可以认为是 Kerberos 世界的用户名，用于标识身份。principal 主要由三部分构成：primary，instance(可选) 和 realm。包含 instance 的 principal，一般会作为 server 端的 principal，如：Zookeeper，NameNode，HiverServer 等；不含有 instance 的 principal，一般会作为客户端的 principal，用于身份认证.
* ![[Pasted image 20220630183344.png]]
## 2.2、Keytab
相当于“密码本”，包含了多个 principal 与密码的文件，用户可以利用该文件进行身份认证。
## 2.3、Ticket Cache
