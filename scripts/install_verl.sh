#!/bin/bash
# -*- coding: utf-8 -*-
# VERL 安装脚本

set -e  # 遇到错误时退出

echo "=== VERL 安装脚本 ==="

# 获取脚本所在目录的父目录（项目根目录）
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
THIRD_PARTY_DIR="${PROJECT_ROOT}/third_party"
VERL_DIR="${THIRD_PARTY_DIR}/verl"

echo "项目根目录: ${PROJECT_ROOT}"
echo "第三方包目录: ${THIRD_PARTY_DIR}"
echo "VERL 目录: ${VERL_DIR}"

# 检查第三方包目录是否存在
if [ ! -d "${THIRD_PARTY_DIR}" ]; then
    echo "❌ 第三方包目录不存在: ${THIRD_PARTY_DIR}"
    echo "请确保在正确的项目目录中运行此脚本"
    exit 1
fi

# 创建 VERL 目录
echo "\\n1. 创建 VERL 目录..."
mkdir -p "${VERL_DIR}"

# 检查是否已经安装了 git
if ! command -v git &> /dev/null; then
    echo "❌ Git 未安装，请先安装 Git"
    exit 1
fi

# 克隆 VERL 仓库
echo "\\n2. 克隆 VERL 仓库..."
if [ -d "${VERL_DIR}/.git" ]; then
    echo "VERL 仓库已存在，更新代码..."
    cd "${VERL_DIR}"
    git pull
else
    echo "克隆 VERL 仓库..."
    git clone https://github.com/volcengine/verl.git "${VERL_DIR}"
fi

# 检查克隆是否成功
if [ ! -f "${VERL_DIR}/setup.py" ] && [ ! -f "${VERL_DIR}/pyproject.toml" ]; then
    echo "❌ VERL 克隆失败，未找到安装文件"
    exit 1
fi

echo "✅ VERL 仓库克隆/更新成功"

# 安装 VERL
echo "\\n3. 安装 VERL..."
cd "${VERL_DIR}"

# 检查是否有 requirements.txt
if [ -f "requirements.txt" ]; then
    echo "安装 VERL 依赖..."
    pip install -r requirements.txt
fi

# 以开发模式安装 VERL
echo "以开发模式安装 VERL..."
pip install -e .

echo "\\n4. 验证安装..."
cd "${PROJECT_ROOT}"

# 运行验证脚本
if [ -f "examples/verl_integration.py" ]; then
    echo "运行 VERL 集成验证..."
    python examples/verl_integration.py
else
    echo "⚠️ 验证脚本不存在，跳过验证"
fi

echo "\\n=== VERL 安装完成 ==="
echo "💡 提示："
echo "   - VERL 已安装到: ${VERL_DIR}"
echo "   - 可以运行 'python examples/verl_integration.py' 来测试集成"
echo "   - 更多信息请查看: https://verl.readthedocs.io/en/latest/index.html"