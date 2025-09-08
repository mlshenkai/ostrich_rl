#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERL 集成示例
演示如何在项目中集成和使用 VERL 框架
"""

import sys
import os

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from ostrich_rl.utils import setup_verl_path, import_verl, check_verl_installation


def main():
    """主函数"""
    print("=== VERL 集成示例 ===")
    
    # 1. 检查 VERL 安装状态
    print("\\n1. 检查 VERL 安装状态...")
    if not check_verl_installation():
        print("❌ VERL 未安装或安装不正确")
        print("请按照以下步骤安装 VERL:")
        print("cd third_party/verl")
        print("git clone https://github.com/volcengine/verl.git .")
        print("pip install -e .")
        return
    
    print("✅ VERL 安装检查通过")
    
    # 2. 设置 VERL 路径
    print("\\n2. 设置 VERL 路径...")
    try:
        verl_path = setup_verl_path()
        print(f"VERL 路径: {verl_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        return
    
    # 3. 导入 VERL
    print("\\n3. 导入 VERL...")
    try:
        verl = import_verl()
        print("✅ VERL 导入成功")
        
        # 显示 VERL 的一些基本信息
        if hasattr(verl, '__version__'):
            print(f"VERL 版本: {verl.__version__}")
        
        if hasattr(verl, '__file__'):
            print(f"VERL 模块路径: {verl.__file__}")
        
        # 列出 VERL 的主要模块
        print("\\n4. VERL 主要模块:")
        verl_modules = [attr for attr in dir(verl) if not attr.startswith('_')]
        for module in verl_modules[:10]:  # 只显示前10个
            print(f"  - {module}")
        if len(verl_modules) > 10:
            print(f"  ... 还有 {len(verl_modules) - 10} 个模块")
        
    except ImportError as e:
        print(f"❌ VERL 导入失败: {e}")
        return
    
    # 5. 示例：尝试使用 VERL 的一些基础功能
    print("\\n5. 尝试使用 VERL 基础功能...")
    try:
        # 这里可以添加一些简单的 VERL 使用示例
        # 由于我们不确定具体的 VERL API，这里只是演示如何检查模块
        
        if hasattr(verl, 'config'):
            print("✅ 找到 verl.config 模块")
        
        if hasattr(verl, 'trainer'):
            print("✅ 找到 verl.trainer 模块")
        
        if hasattr(verl, 'models'):
            print("✅ 找到 verl.models 模块")
        
        print("\\n💡 提示: 具体的 VERL 使用方法请参考 VERL 官方文档")
        print("   文档地址: https://verl.readthedocs.io/en/latest/index.html")
        
    except Exception as e:
        print(f"⚠️ 使用 VERL 时遇到问题: {e}")
    
    print("\\n=== 示例运行完成 ===")


if __name__ == "__main__":
    main()