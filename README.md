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
        "admin": "yes"
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
curl -X POST http://localhost:8080/post \
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
curl http://localhost:8080
```

##### 根据版块名查看版块内容

```shell
curl http://localhost:8080/show/section1
```

##### 删除一个版块

```shell
curl http://localhost:8080/delete/section1
```

### issues

1、目前用户和版块没有建立关系，因此“ 非管理员无法管理版块” 的要求没有实现；

2、删除版块的二次确认含义不明：

​	1）调用 API 后再次要求用户输入 y/n 确认是否删除 

​	2）同一资源第二次删除时捕获异常并报错                                      
