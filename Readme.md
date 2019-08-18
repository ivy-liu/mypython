
* Python 绝对路径引用
===
问题：  
Python开发时经常出现找不到import对象的问题，ImportError: No module named xxx，一般的原因不外乎  
  
未安装对应依赖  
引用对象的文件夹下缺失 __init__.py文件  
由于通过相对路径的加载，导致找不到object  
解决方法  
针对原因1和2通过安装依赖和添加__init__.py文件即可。原因3我们的解决方法是把相对路径的import改为绝对路径。  

假定文件结构如下：  
```python
project:
    |__ src/
        |__ main.py
    |__ common/
        |__ utils.py
 ```
 在main.py中引用utils.py的方法，相对路径的引用示例：  
 ```python
 # -*- coding=utf-8 -*-
import os
import sys

# 相对路径的import
sys.path.append("../")
from common.utils import *


if __name__ == "__main__":
    print(os.path.dirname(__file__))

 ```
 在文件结构复杂的项目中，相对路径的引用存在找不到引用对象的可能，为此修改为绝对路径引用，示例如下：  
 ```python
 # -*- coding=utf-8 -*-
import os
import sys

# 绝对路径的import
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from common.utils import *


if __name__ == "__main__":
    print(os.path.dirname(os.path.abspath(__file__)))

 ```
 
