# Ostrich RL

基于 VERL (Volcano Engine Reinforcement Learning) 的强化学习项目。

## 项目简介

本项目是一个强化学习框架，集成了 VERL 作为核心强化学习引擎，用于大语言模型的强化学习训练。

## 项目结构

```
ostrich_rl/
├── docs/                   # 文档目录
├── examples/               # 示例代码
├── recipe/                 # 训练配方和配置
├── scripts/                # 实用脚本
├── tests/                  # 测试代码
├── third_party/            # 第三方依赖
│   └── verl/              # VERL 框架
├── ostrich_rl/            # 主要代码库
├── requirements.txt        # Python 依赖
├── setup.py               # 安装配置
└── README.md              # 项目说明
```

## 安装

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd ostrich_rl
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 安装 VERL

```bash
cd third_party/verl
git clone https://github.com/volcengine/verl.git .
pip install -e .
cd ../..
```

### 4. 安装本项目

```bash
pip install -e .
```

## 快速开始

请参考 `examples/` 目录中的示例代码。

## 文档

详细文档请查看 `docs/` 目录。

## 致谢

本项目基于 [VERL](https://github.com/volcengine/verl) 框架构建，感谢 Volcano Engine 团队的贡献。

## 许可证

请参考 LICENSE 文件。