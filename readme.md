1. 安装 
`python2.7`, `pip`

2. 安装依赖 
`pip install -r requirements.txt`

3. 然后新建project/instance/文件夹，创建两个文件`__init__.py`, `config.py`

`config.py`内容如下：

```
# -*- coding: utf-8 -*-
# config for db/key, etc -- private & personal
DEBUG = True
SECRET_KEY = 'your own scret key'
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@ip/dbname'
```

4. 首次需要执行init_db.py，初始化数据库

