# 基本概念
## 镜像（Image）
[参考链接](https://cloud.tencent.com/developer/article/1772136)
Docker镜像是一个特殊的文件系统，除了提供容器运行时的程序、库、资源、配置等文件外，还包含一些为运行时准备的配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建后也不会改变
## 容器（Container）
镜像-容器，好比是面向对象里面的类-对象实例，镜像是静态的定义，容器是镜像的运行时的实体。容器可以被创建，启动，停止，删除，暂停
## 仓库（Repository）
类似于git仓库的远程仓库，集中存放镜像文件
![[Pasted image 20220704195554.png]]
## 常用命令
![[Pasted image 20220705190914.png]]
* docker version （docker -v）
* systemctl start docker  启动Docker
* systemctl stop docker  关闭Docker
* systemctl enable docker  设置开机自启
* service docker restart  重启docker服务
* service docker stop 关闭docker服务*