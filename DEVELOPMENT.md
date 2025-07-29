# 音乐白皮书项目开发指南

## 🚀 快速开始

### 1. 环境设置
```bash
# 安装依赖
pip3 install -r requirements.txt

# 设置开发环境
export PATH=$PATH:/Users/ma/.local/bin
python3 dev_tools.py setup
```

### 2. 代码开发
```bash
# 格式化代码
python3 dev_tools.py format

# 检查代码质量
python3 dev_tools.py check

# 运行测试
python3 dev_tools.py test
```

## 🔧 开发工具

### 代码质量工具
- **Black**: Python代码格式化
- **isort**: 导入语句排序
- **pylint**: 代码质量检查
- **pre-commit**: Git提交前检查

### 自动化工具
- **scheduler_simple.py**: 简化版调度器
- **scheduler.py**: 完整版调度器
- **dev_tools.py**: 开发工具脚本

## 📋 项目结构

```
music_whitepaper_project/
├── analysis/           # 数据分析模块
├── content/           # 内容生成模块
├── data/              # 数据存储
├── reports/           # 生成的报告
├── visualization/     # 可视化模块
├── config/           # 配置文件
├── docs/             # 文档
├── .github/          # GitHub Actions
├── .vscode/          # VS Code配置
├── dev_tools.py      # 开发工具
├── scheduler.py      # 自动化调度器
└── requirements.txt  # 依赖列表
```

## 🎯 自动化功能

### 定时生成报告
- **周报**: 每周一上午9点
- **月报**: 每月1号上午10点
- **季报**: 每季度第一天上午11点

### 手动生成报告
```bash
# 生成周报
python3 scheduler_simple.py weekly

# 生成月报
python3 scheduler_simple.py monthly

# 生成季报
python3 scheduler_simple.py quarterly
```

## 🔄 Git工作流

### 提交代码
```bash
# 添加文件
git add .

# 提交更改
git commit -m "描述更改"

# 推送到GitHub
git push origin main
```

### 代码质量检查
项目已配置pre-commit钩子，会在提交前自动：
- 格式化代码（Black）
- 排序导入（isort）
- 检查代码质量（pylint）

## 📊 监控和日志

### 查看日志
```bash
# 查看调度器日志
tail -f scheduler.log

# 查看GitHub Actions
# 访问: https://github.com/mazhezhema/music_whitepaper/actions
```

### 生成的文件
- **报告**: `reports/` 目录
- **图表**: `visualization/charts/` 目录
- **数据**: `data/processed/` 目录

## 🛠️ 故障排除

### 常见问题

1. **代理连接问题**
   - 使用SSH推送：`git remote set-url origin git@github.com:mazhezhema/music_whitepaper.git`
   - 配置SSH密钥

2. **代码格式化问题**
   - 运行：`python3 dev_tools.py format`
   - 检查：`python3 dev_tools.py check`

3. **依赖安装问题**
   - 确保使用Python 3.8+
   - 检查PATH设置：`export PATH=$PATH:/Users/ma/.local/bin`

## 📞 支持

- **项目地址**: https://github.com/mazhezhema/music_whitepaper
- **问题反馈**: 在GitHub Issues中提交
- **文档**: 查看 `docs/` 目录

---

**祝您开发愉快！** 🎉 