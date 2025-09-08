# -*- coding: utf-8 -*-
"""
基础配置类
提供项目的基础配置管理功能
"""

import os
import yaml
from typing import Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class BaseConfig:
    """
    基础配置类
    """
    # 项目基础配置
    project_name: str = "ostrich_rl"
    version: str = "0.1.0"
    
    # VERL 相关配置
    verl_path: Optional[str] = None
    use_verl: bool = True
    
    # 训练相关配置
    batch_size: int = 32
    learning_rate: float = 1e-5
    num_epochs: int = 10
    save_steps: int = 500
    
    # 模型相关配置
    model_name: str = ""
    model_path: str = ""
    
    # 输出配置
    output_dir: str = "./outputs"
    log_dir: str = "./logs"
    
    # 其他配置
    seed: int = 42
    device: str = "auto"  # auto, cpu, cuda
    
    def __post_init__(self):
        """初始化后处理"""
        # 确保输出目录存在
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
    
    @classmethod
    def from_yaml(cls, yaml_path: str) -> "BaseConfig":
        """
        从 YAML 文件加载配置
        
        Args:
            yaml_path: YAML 配置文件路径
            
        Returns:
            BaseConfig: 配置实例
        """
        with open(yaml_path, 'r', encoding='utf-8') as f:
            config_dict = yaml.safe_load(f)
        
        return cls(**config_dict)
    
    def to_yaml(self, yaml_path: str):
        """
        将配置保存到 YAML 文件
        
        Args:
            yaml_path: 保存路径
        """
        config_dict = self.__dict__.copy()
        
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f, default_flow_style=False, 
                     allow_unicode=True, indent=2)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        转换为字典
        
        Returns:
            Dict[str, Any]: 配置字典
        """
        return self.__dict__.copy()
    
    def update(self, **kwargs):
        """
        更新配置参数
        
        Args:
            **kwargs: 要更新的配置参数
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"未知的配置参数: {key}")