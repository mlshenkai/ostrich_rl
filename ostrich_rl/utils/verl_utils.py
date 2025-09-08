# -*- coding: utf-8 -*-
"""
VERL 集成工具
提供与 VERL 框架集成的实用函数
"""

import os
import sys
from typing import Optional


def setup_verl_path(project_root: Optional[str] = None) -> str:
    """
    设置 VERL 库的路径到 Python 系统路径中
    
    Args:
        project_root: 项目根目录路径，如果为 None 则自动检测
        
    Returns:
        str: VERL 库的路径
    """
    if project_root is None:
        # 自动检测项目根目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
    
    verl_path = os.path.join(project_root, "third_party", "verl")
    
    if not os.path.exists(verl_path):
        raise FileNotFoundError(
            f"VERL 路径不存在: {verl_path}\\n"
            f"请确保已经按照 README.md 中的说明安装了 VERL"
        )
    
    if verl_path not in sys.path:
        sys.path.insert(0, verl_path)
    
    return verl_path


def import_verl():
    """
    导入 VERL 库
    
    Returns:
        module: VERL 模块
        
    Raises:
        ImportError: 如果无法导入 VERL
    """
    try:
        setup_verl_path()
        import verl
        return verl
    except ImportError as e:
        raise ImportError(
            f"无法导入 VERL: {e}\\n"
            f"请确保已经按照 README.md 中的说明正确安装了 VERL"
        )


def check_verl_installation() -> bool:
    """
    检查 VERL 是否正确安装
    
    Returns:
        bool: 如果 VERL 正确安装返回 True，否则返回 False
    """
    try:
        import_verl()
        return True
    except (ImportError, FileNotFoundError):
        return False


def get_verl_version() -> Optional[str]:
    """
    获取 VERL 版本信息
    
    Returns:
        Optional[str]: VERL 版本号，如果无法获取则返回 None
    """
    try:
        verl = import_verl()
        return getattr(verl, "__version__", None)
    except (ImportError, FileNotFoundError):
        return None