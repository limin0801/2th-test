# Python 第二次考试编程题代码

## q1

编程题第一题

user_registory.py # 用户注册

login.py # 用户登录

## q2 

编程题第二题

是一个完整的 pecan 项目，建立了用户表和论坛版块表。

版块实现了创建、查找、删除的功能。 

用户主要用到创建、登录的功能。

### 项目运行
```shell
cd q2_bbs

# 安装
python setup.py install

# 开发调试
python setup.py develop

# 启动项目
pecan serve config.py
```
### 数据库注意事项
默认使用 mysql 数据库，在 `q2_bbs/q2_bbs/database/__init__.py` 文件中可以自行修改数据库用户名、密码、数据库名称。

若使用虚拟环境，默认没有安装 pymysql，可自行使用 pip 进行安装。

### API 调用

#### 用户

##### 创建一个用户

```shell
curl -X POST http://localhost:8080/user/post \
-H "Content-Type: application/json" \
-d \
'{
    "user": {
        "name": "user1",
        "passwd": "test1",
        "admin": true
    }
}'
```

##### 用户登录

```shell
curl http://localhost:8080/user/login \
-H "Content-Type: application/json" \
-d \
'{
    "user": {
        "name": "user1",
        "passwd": "test1"
    }
}'  
```

#### 版块

##### 创建一个版块

```shell
curl -X POST http://localhost:8080/section/post \
-H "Content-Type: application/json" \
-d \
'{
    "section": {
        "name": "section1",
        "description": "this is test description of section1"
    }
}' 
```

##### 查看所有版块

```shell
curl http://localhost:8080/section/
```

##### 根据版块名查看版块内容

```shell
curl http://localhost:8080/section/show/section1
```

##### 删除一个版块

```shell
curl http://localhost:8080/section/delete/section1
```

