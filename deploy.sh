#!/bin/bash

# 音乐白皮书项目部署脚本

echo "🚀 开始部署音乐白皮书自动化项目..."

# 检查Python版本
python_version=$(python3 --version 2>&1)
echo "📦 Python版本: $python_version"

# 安装依赖
echo "📥 安装Python依赖..."
pip3 install -r requirements.txt

# 设置Git配置
echo "🔧 配置Git..."
git config user.name "mazhezhema"
git config user.email "mazhezhema@github.com"

# 创建必要的目录
echo "📁 创建必要的目录..."
mkdir -p logs
mkdir -p data/raw
mkdir -p data/processed
mkdir -p reports
mkdir -p visualization/charts

# 设置文件权限
echo "🔐 设置文件权限..."
chmod +x scheduler.py
chmod +x main.py

# 初始化Git仓库（如果还没有）
if [ ! -d ".git" ]; then
    echo "🔧 初始化Git仓库..."
    git init
    git remote add origin https://github.com/mazhezhema/music_whitepaper_project.git
fi

# 提交初始代码
echo "💾 提交代码到Git..."
git add .
git commit -m "Initial deployment: Music whitepaper automation project"
git push -u origin main

echo "✅ 部署完成！"
echo ""
echo "📋 使用说明："
echo "1. 手动生成报告: python scheduler.py [weekly|monthly|quarterly]"
echo "2. 启动自动调度: python scheduler.py run"
echo "3. 查看日志: tail -f scheduler.log"
echo ""
echo "🔄 GitHub Actions已配置，将自动在以下时间生成报告："
echo "   - 每周一上午9点：周报"
echo "   - 每月1号上午10点：月报"
echo "   - 每季度第一天上午11点：季报"
echo ""
echo "🌐 项目地址: https://github.com/mazhezhema/music_whitepaper_project" 