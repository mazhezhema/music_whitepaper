# GitHub 仓库设置指南

## 🚀 项目自动化功能已配置完成

您的音乐白皮书项目已经配置了完整的自动化功能，包括：

### ✅ 已完成的配置

1. **自动化调度器** (`scheduler.py`)
   - 每周一上午9点生成周报
   - 每月1号上午10点生成月报
   - 每季度第一天上午11点生成季报

2. **GitHub Actions** (`.github/workflows/auto-generate.yml`)
   - 自动在指定时间运行
   - 支持手动触发生成报告

3. **部署脚本** (`deploy.sh`)
   - 一键部署所有功能
   - 自动配置Git和依赖

## 📋 下一步操作

### 1. 在GitHub上创建仓库

1. 访问 https://github.com/mazhezhema
2. 点击 "New repository"
3. 仓库名称: `music_whitepaper_project`
4. 设置为 Public 或 Private
5. 不要初始化README（因为我们已经有了）

### 2. 推送代码到GitHub

当网络连接正常时，运行以下命令：

```bash
# 确保在项目目录中
cd /Users/ma/music_whitepaper_project

# 推送代码
git push -u origin main
```

### 3. 启用GitHub Actions

1. 在GitHub仓库页面，点击 "Actions" 标签
2. 点击 "Enable Actions"
3. 选择 "Allow all actions and reusable workflows"

### 4. 测试自动化功能

#### 手动测试
```bash
# 生成周报
python scheduler.py weekly

# 生成月报
python scheduler.py monthly

# 生成季报
python scheduler.py quarterly
```

#### 启动本地调度器
```bash
# 启动自动调度（后台运行）
python scheduler.py run
```

### 5. 查看自动化结果

- **本地日志**: `tail -f scheduler.log`
- **GitHub Actions**: 在仓库的Actions标签页查看运行状态
- **生成的文件**: 在 `reports/` 目录中查看生成的报告

## 🔧 配置说明

### 自动化时间表
- **周报**: 每周一上午9点
- **月报**: 每月1号上午10点
- **季报**: 每季度第一天上午11点

### 文件命名规则
- 周报: `weekly_report_YYYYMMDD_YYYYMMDD.md`
- 月报: `monthly_report_YYYYMM.md`
- 季报: `quarterly_report_YYYYQQ.md`

### 自动Git提交
每次生成报告后，系统会自动：
1. 添加新生成的文件
2. 提交到Git
3. 推送到GitHub仓库

## 📞 故障排除

### 如果推送失败
```bash
# 检查网络连接
ping github.com

# 使用SSH密钥（推荐）
git remote set-url origin git@github.com:mazhezhema/music_whitepaper_project.git
```

### 如果GitHub Actions不工作
1. 检查仓库设置中的Actions权限
2. 确保工作流文件在 `.github/workflows/` 目录中
3. 查看Actions日志获取错误信息

## 🎯 项目优势

1. **完全自动化**: 无需手动干预，定期生成报告
2. **版本控制**: 所有报告都有Git历史记录
3. **可追溯**: 每次生成都有时间戳和日志
4. **可扩展**: 易于添加新的报告类型
5. **云原生**: 使用GitHub Actions，无需本地服务器

## 📊 监控和日志

- **调度器日志**: `scheduler.log`
- **GitHub Actions日志**: 在GitHub仓库的Actions页面
- **生成报告**: `reports/` 目录
- **数据文件**: `data/processed/` 目录

---

**项目地址**: https://github.com/mazhezhema/music_whitepaper_project

**自动化状态**: ✅ 已配置完成，等待GitHub仓库创建后即可使用 