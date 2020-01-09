# AndroLuaBox

**这是一个AndroLua教程的web服务**

## 一、文件夹说明

- SQL：数据库备份
- api：Python Django后端服务
- web：Vue前端

## 二、服务部署

### 1. 前端

**前端文件直接部署，使用nginx,apache等直接访问即可。**

> 此前端直接使用CDN的方式编写，并未使用vue-cli，故前端源代码会暴露，存在一定的安全问题，动手能力强的同学可自行更改，也可只部署后端，使用api

### 2. 后端

**后端使用Django框架进行编写，下面是部署流程：（以Ubuntu为例）**

**请先安装MySQL和导入数据库备份文件，并更改后端文件中的setting.py文件，将数据库的用户和密码添加进去，再进行以下操作。**

1. 安装Python3与pip

`sudo apt-get install python3 python3-pip`

2. 安装Django和mysqlclient

`pip install django `

`pip install mysqlclient`

3. 直接运行服务即可

`python3  manage.py runserver 0.0.0.0:8000`

**当前开源项目是通过uwsgi+nginx进行部署，部署方法较复杂，自行百度，故上述方法是无法连通前端，请自行更改前端文件对应链接**

## 三、效果展示

链接：http://alua.hfybbs.vip/

### 截图：

![](https://i.loli.net/2020/01/09/8aCp3FrHeTfwmAL.png)

![image.png](https://i.loli.net/2020/01/09/2o9sLwek3rdxWVz.png)

![image.png](https://i.loli.net/2020/01/09/n26Q8LaxOj7kTCV.png)

![image.png](https://i.loli.net/2020/01/09/mS8IoMfPTAaNw75.png)