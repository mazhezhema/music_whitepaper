#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音乐行业白皮书项目主程序
整合数据分析、文案生成、可视化等功能
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, List

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis.data_analyzer import MusicDataAnalyzer
from content.content_generator import ContentGenerator
from visualization.chart_generator import ChartGenerator

class MusicWhitepaperProject:
    """音乐白皮书项目主控制器"""
    
    def __init__(self):
        self.analyzer = MusicDataAnalyzer()
        self.content_generator = ContentGenerator()
        self.chart_generator = ChartGenerator()
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        
    def setup_project_structure(self):
        """设置项目目录结构"""
        directories = [
            'data/raw',
            'data/processed',
            'analysis',
            'reports',
            'content',
            'visualization/charts',
            'config',
            'docs'
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            print("✓ 创建目录: {}".format(directory))
    
    def process_raw_data(self, data_file: str) -> Dict:
        """处理原始数据"""
        print("📊 开始处理原始数据: {}".format(data_file))
        
        # 加载数据
        data = self.analyzer.load_billboard_data(data_file)
        
        # 生成分析报告
        analysis_report = self.analyzer.generate_comprehensive_report()
        
        # 保存分析结果
        output_path = 'analysis/comprehensive_analysis.json'
        self.analyzer.save_analysis_results(output_path)
        
        print("✓ 数据分析完成，结果保存到: {}".format(output_path))
        return analysis_report
    
    def generate_reports(self, analysis_data: Dict):
        """生成各种报告"""
        print("📝 开始生成报告...")
        
        # 生成完整白皮书
        whitepaper = self.content_generator.generate_complete_whitepaper(analysis_data)
        self.content_generator.save_report(whitepaper, 'reports/music_whitepaper_2025q2.md')
        print("✓ 完整白皮书已生成")
        
        # 生成执行摘要
        executive_summary = self.content_generator.generate_executive_summary(analysis_data)
        self.content_generator.save_report(executive_summary, 'reports/executive_summary.md')
        print("✓ 执行摘要已生成")
        
        # 生成营销文案
        marketing_copy = self.content_generator.generate_marketing_copy()
        self.content_generator.save_report(marketing_copy, 'reports/marketing_copy.md')
        print("✓ 营销文案已生成")
        
        # 生成技术规格文档
        technical_specs = self.content_generator.generate_technical_specs()
        self.content_generator.save_report(technical_specs, 'reports/technical_specs.md')
        print("✓ 技术规格文档已生成")
    
    def generate_visualizations(self, analysis_data: Dict):
        """生成可视化图表"""
        print("📈 开始生成可视化图表...")
        
        chart_paths = self.chart_generator.generate_all_charts(analysis_data)
        
        for chart_name, path in chart_paths.items():
            print("✓ {} 图表已生成: {}".format(chart_name, path))
    
    def create_project_summary(self):
        """创建项目总结"""
        summary = f"""
# 音乐行业白皮书项目总结

## 项目概述
本项目基于雷石K歌全系列终端数据，为硬件厂商提供专业的音乐行业市场洞察和商业建议。

## 生成的文件
- `reports/music_whitepaper_2025q2.md` - 完整白皮书
- `reports/executive_summary.md` - 执行摘要
- `reports/marketing_copy.md` - 营销文案
- `reports/technical_specs.md` - 技术规格
- `analysis/comprehensive_analysis.json` - 分析数据
- `visualization/charts/` - 可视化图表

## 核心发现
1. 情绪类曲目占据排行榜主导地位
2. 女性用户占比42%，但女性独唱内容需求持续上升
3. 三线城市播放量季度增长19%，下沉市场潜力巨大
4. 家庭娱乐设备使用时长平均提升15分钟

## 商业建议
1. 情绪分区K歌系统开发
2. 地域特色内容定制
3. 智能推荐算法优化
4. 硬件厂商合作授权
5. 数据服务商业化

## 生成时间
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---
*本项目由雷石互联网研究院出品*
"""
        
        with open('docs/project_summary.md', 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print("✓ 项目总结已生成")
    
    def run_complete_pipeline(self, data_file: str = None):
        """运行完整的处理流程"""
        print("🚀 开始音乐行业白皮书项目处理流程...")
        
        # 设置项目结构
        self.setup_project_structure()
        
        # 确定数据文件路径
        if data_file is None:
            data_file = 'data/raw/billboard_report_2025q2.md'
        
        # 检查数据文件是否存在
        if not os.path.exists(data_file):
            print("❌ 数据文件不存在: {}".format(data_file))
            return
        
        # 处理原始数据
        analysis_data = self.process_raw_data(data_file)
        
        # 生成报告
        self.generate_reports(analysis_data)
        
        # 生成可视化
        self.generate_visualizations(analysis_data)
        
        # 创建项目总结
        self.create_project_summary()
        
        print("\n🎉 项目处理完成！")
        print("\n生成的文件:")
        print("- reports/music_whitepaper_2025q2.md (完整白皮书)")
        print("- reports/executive_summary.md (执行摘要)")
        print("- reports/marketing_copy.md (营销文案)")
        print("- reports/technical_specs.md (技术规格)")
        print("- visualization/charts/ (可视化图表)")
        print("- docs/project_summary.md (项目总结)")
    
    def generate_custom_report(self, report_type: str, analysis_data: Dict = None):
        """生成定制化报告"""
        if analysis_data is None:
            # 加载分析数据
            try:
                with open('analysis/comprehensive_analysis.json', 'r', encoding='utf-8') as f:
                    analysis_data = json.load(f)
            except FileNotFoundError:
                print("❌ 分析数据文件不存在，请先运行完整流程")
                return
        
        print("📋 生成定制化报告: {}".format(report_type))
        
        if report_type == 'whitepaper':
            content = self.content_generator.generate_complete_whitepaper(analysis_data)
            output_path = 'reports/custom_whitepaper.md'
        elif report_type == 'executive':
            content = self.content_generator.generate_executive_summary(analysis_data)
            output_path = 'reports/custom_executive.md'
        elif report_type == 'marketing':
            content = self.content_generator.generate_marketing_copy()
            output_path = 'reports/custom_marketing.md'
        elif report_type == 'technical':
            content = self.content_generator.generate_technical_specs()
            output_path = 'reports/custom_technical.md'
        else:
            print(f"❌ 未知的报告类型: {report_type}")
            return
        
        self.content_generator.save_report(content, output_path)
        print("✓ 定制化报告已生成: {}".format(output_path))

def main():
    """主函数"""
    project = MusicWhitepaperProject()
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'run':
            # 运行完整流程
            data_file = sys.argv[2] if len(sys.argv) > 2 else None
            project.run_complete_pipeline(data_file)
        
        elif command == 'report':
            # 生成定制化报告
            if len(sys.argv) > 2:
                report_type = sys.argv[2]
                project.generate_custom_report(report_type)
            else:
                print("请指定报告类型: whitepaper, executive, marketing, technical")
        
        elif command == 'help':
            print("""
音乐行业白皮书项目使用说明:

1. 运行完整流程:
   python main.py run [数据文件路径]

2. 生成定制化报告:
   python main.py report [报告类型]
   报告类型: whitepaper, executive, marketing, technical

3. 查看帮助:
   python main.py help
            """)
        
        else:
            print("未知命令: {}".format(command))
            print("使用 'python main.py help' 查看帮助")
    
    else:
        # 默认运行完整流程
        project.run_complete_pipeline()

if __name__ == "__main__":
    main() 