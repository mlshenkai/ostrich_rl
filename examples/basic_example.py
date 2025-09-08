#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础使用示例
演示如何使用 Ostrich RL 框架的基本功能
"""

import sys
import os

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from ostrich_rl.config import BaseConfig
from ostrich_rl.utils import check_verl_installation, get_verl_version


def main():
    """主函数"""
    print("=== Ostrich RL 基础示例 ===")
    
    # 1. 创建配置
    print("\\n1. 创建配置...")
    config = BaseConfig(
        project_name="basic_example",
        batch_size=16,
        learning_rate=2e-5,
        output_dir="./outputs/basic_example"
    )
    print(f"配置创建完成: {config.project_name}")
    
    # 2. 检查 VERL 安装状态
    print("\\n2. 检查 VERL 安装状态...")
    if check_verl_installation():
        version = get_verl_version()
        print(f"✅ VERL 已正确安装，版本: {version or '未知'}")
    else:
        print("❌ VERL 未安装或安装不正确")
        print("请参考 README.md 中的安装说明")
    
    # 3. 显示配置信息
    print("\\n3. 配置信息:")
    config_dict = config.to_dict()
    for key, value in config_dict.items():
        print(f"  {key}: {value}")
    
    # 4. 保存配置到文件
    config_file = os.path.join(config.output_dir, "config.yaml")
    config.to_yaml(config_file)
    print(f"\\n4. 配置已保存到: {config_file}")
    
    print("\\n=== 示例运行完成 ===")


if __name__ == "__main__":
    main()