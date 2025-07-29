#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
开发工具脚本
提供代码格式化、检查、测试等功能
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """运行命令并显示结果"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} 完成")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description} 失败")
            if result.stderr:
                print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ {description} 出错: {e}")
        return False


def format_code():
    """格式化代码"""
    print("🎨 代码格式化工具")
    print("=" * 50)

    # 格式化Python代码
    run_command("black .", "Black 格式化")
    run_command("isort .", "isort 导入排序")

    print("✅ 代码格式化完成")


def check_code():
    """检查代码质量"""
    print("🔍 代码质量检查")
    print("=" * 50)

    # 运行pylint
    run_command(
        "pylint *.py analysis/*.py content/*.py visualization/*.py", "Pylint 代码检查"
    )

    print("✅ 代码质量检查完成")


def run_tests():
    """运行测试"""
    print("🧪 运行测试")
    print("=" * 50)

    # 测试调度器
    run_command("python3 scheduler_simple.py weekly", "测试周报生成")

    print("✅ 测试完成")


def setup_dev():
    """设置开发环境"""
    print("🛠️ 设置开发环境")
    print("=" * 50)

    # 安装依赖
    run_command("pip3 install -r requirements.txt", "安装依赖")

    # 设置pre-commit
    run_command("pre-commit install", "安装pre-commit钩子")

    print("✅ 开发环境设置完成")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python3 dev_tools.py [format|check|test|setup]")
        print("\n可用命令:")
        print("  format  - 格式化代码")
        print("  check   - 检查代码质量")
        print("  test    - 运行测试")
        print("  setup   - 设置开发环境")
        return

    command = sys.argv[1]

    if command == "format":
        format_code()
    elif command == "check":
        check_code()
    elif command == "test":
        run_tests()
    elif command == "setup":
        setup_dev()
    else:
        print(f"❌ 未知命令: {command}")


if __name__ == "__main__":
    main()
