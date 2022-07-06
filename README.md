# UI_test
PO设计模式
1. base--基类定义
   1. BasePage基类
      1. 封装driver基本操作
         1. 新建driver(复用)
         2. 元素查找, 点击,输入 等
2. comm_utils--通用组件
   1. config.py  读取配置文件及环境变量
   2. log.py 日志模块
3. config--配置文件存放
4. page--具体业务页面定义
   1. 每一个页面均定义一个类
   2. 对外提供每个页面上可进行操作的方法
   3. 不暴露页面具体元素
   4. 页面发生改动, 仅需修改Locator
   5. 页面跳转也可以return newPage(driver)
5. test_scripts--测试脚本
   1. 根目录下定义conftest.py
      1. 加载环境变量
      2. 启动, 复用, 关闭driver
6. run.py & run.sh & single_run.py -- 入口脚本