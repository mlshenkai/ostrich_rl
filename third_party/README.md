# 第三方包目录

此目录包含项目依赖的第三方库和工具。

## 目录结构

- `verl/`: Volcano Engine Reinforcement Learning for LLMs
  - 用于大语言模型强化学习的框架
  - 项目地址: https://github.com/volcengine/verl.git

## 安装说明

### 安装 verl

```bash
cd third_party/verl
git clone https://github.com/volcengine/verl.git .
pip install -e .
```

## 使用方法

在项目中引用第三方包：

```python
# 添加第三方包路径到系统路径
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'third_party'))

# 导入 verl
from verl import ...
```