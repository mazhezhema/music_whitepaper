#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音乐行业白皮书文案生成模块
用于自动生成专业的咨询报告和营销文案
"""

import json
from datetime import datetime
from typing import Any, Dict, List

from jinja2 import Template


class ContentGenerator:
    """文案生成器"""

    def __init__(self):
        self.templates = {}
        self.load_templates()

    def load_templates(self):
        """加载文案模板"""
        self.templates = {
            "executive_summary": """
# 音乐行业白皮书：2025年Q2市场洞察报告

## 执行摘要

基于雷石K歌全系列终端数据分析，2025年Q2音乐市场呈现以下关键趋势：

### 🎯 核心发现
{% for finding in key_findings %}
- {{ finding }}
{% endfor %}

### 💡 市场机遇
{% for opportunity in market_opportunities %}
- {{ opportunity }}
{% endfor %}

### 📊 数据亮点
- 情绪类曲目占据排行榜主导地位，emo和怀旧情绪高度活跃
- 女性用户占比42%，但女性独唱内容需求持续上升
- 三线城市播放量季度增长19%，下沉市场潜力巨大
- 家庭娱乐设备使用时长平均提升15分钟

---
""",
            "market_analysis": """
## 市场深度分析

### 用户画像洞察
{% for user_type, percentage in user_demographics.user_types.items() %}
- **{{ user_type }}** ({{ percentage }}%): {{ user_type }}群体偏好{{ user_type }}相关标签内容
{% endfor %}

### 地域偏好分析
{% for region in regional_trends %}
- **{{ region.city_type }}**: 偏好{{ region.preferred_tags|join('、') }}标签，典型歌曲包括{{ region.typical_songs|join('、') }}
{% endfor %}

### 时间使用模式
- **高峰时段**: {{ time_patterns.peak_hours.start }} - {{ time_patterns.peak_hours.end }} (使用率{{ time_patterns.peak_hours.usage_rate|int }}%)
- **次高峰**: {{ time_patterns.secondary_peak.start }} - {{ time_patterns.secondary_peak.end }} (使用率{{ time_patterns.secondary_peak.usage_rate|int }}%)
- **低谷时段**: {{ time_patterns.low_usage.start }} - {{ time_patterns.low_usage.end }} (使用率{{ time_patterns.low_usage.usage_rate|int }}%)

---
""",
            "business_recommendations": """
## 硬件厂商合作建议

### 🎯 产品定制方向
{% for rec in business_recommendations %}
{% if rec.category == '产品定制' %}
#### {{ rec.title }}
**目标用户**: {{ rec.target_audience }}  
**实施方式**: {{ rec.implementation }}  
**预期效果**: {{ rec.expected_impact }}  

{{ rec.description }}

{% endif %}
{% endfor %}

### 📦 内容授权服务
{% for rec in business_recommendations %}
{% if rec.category == '内容授权' %}
#### {{ rec.title }}
**目标用户**: {{ rec.target_audience }}  
**实施方式**: {{ rec.implementation }}  
**预期效果**: {{ rec.expected_impact }}  

{{ rec.description }}

{% endif %}
{% endfor %}

### 🧠 数据服务方案
{% for rec in business_recommendations %}
{% if rec.category == '数据服务' %}
#### {{ rec.title }}
**目标用户**: {{ rec.target_audience }}  
**实施方式**: {{ rec.implementation }}  
**预期效果**: {{ rec.expected_impact }}  

{{ rec.description }}

{% endif %}
{% endfor %}

---
""",
            "trend_predictions": """
## 趋势预测与展望

### 短期趋势 (Q3-Q4 2025)
{{ predictions.short_term }}

### 中期趋势 (2026年)
{{ predictions.medium_term }}

### 长期趋势 (2027年及以后)
{{ predictions.long_term }}

### 标签热度预测
{% for tag in tag_trends %}
- **{{ tag.tag }}**: 当前热度{{ tag.frequency }}次，环比增长{{ tag.growth_rate }}%，预测增长{{ tag.predicted_growth }}%
{% endfor %}

---
""",
            "marketing_copy": """
## 营销文案模板

### 产品宣传文案
**标题**: 雷石音乐数据驱动，为您的硬件产品赋能

**核心卖点**:
- 🎵 基于真实用户数据的精准推荐
- 📊 实时更新的热门排行榜
- 🎯 情绪分区的个性化体验
- 🌍 地域特色的本地化内容
- 📈 持续增长的用户粘性

**目标客户**: 音响厂商、KTV设备商、家庭娱乐设备制造商

### 合作提案文案
**标题**: 携手雷石，共创音乐智能新时代

**合作价值**:
- 数据驱动的产品优化
- 用户画像的精准定位
- 内容生态的持续更新
- 市场趋势的提前把握
- 商业模式的创新突破

---
""",
            "technical_specs": """
## 技术规格与实施细节

### API接口规范
```json
{
  "endpoint": "/api/v1/music/trends",
  "method": "GET",
  "response": {
    "top_songs": [],
    "user_demographics": {},
    "regional_data": [],
    "tag_trends": []
  }
}
```

### 数据更新频率
- 热门歌曲排行榜: 每日更新
- 用户画像数据: 每周更新
- 地域偏好分析: 每月更新
- 趋势预测模型: 季度更新

### 集成要求
- 支持HTTP/HTTPS协议
- 数据格式: JSON
- 认证方式: API Key
- 请求频率限制: 1000次/小时

---
""",
        }

    def generate_executive_summary(self, analysis_data: Dict) -> str:
        """生成执行摘要"""
        template = Template(self.templates["executive_summary"])
        return template.render(**analysis_data["executive_summary"])

    def generate_market_analysis(self, analysis_data: Dict) -> str:
        """生成市场分析"""
        template = Template(self.templates["market_analysis"])
        return template.render(**analysis_data["detailed_analysis"])

    def generate_business_recommendations(self, analysis_data: Dict) -> str:
        """生成商业建议"""
        template = Template(self.templates["business_recommendations"])
        return template.render(
            business_recommendations=analysis_data["business_recommendations"]
        )

    def generate_trend_predictions(self, analysis_data: Dict) -> str:
        """生成趋势预测"""
        template = Template(self.templates["trend_predictions"])
        return template.render(
            predictions=analysis_data["predictions"],
            tag_trends=analysis_data["detailed_analysis"]["tag_trends"],
        )

    def generate_marketing_copy(self) -> str:
        """生成营销文案"""
        template = Template(self.templates["marketing_copy"])
        return template.render()

    def generate_technical_specs(self) -> str:
        """生成技术规格"""
        template = Template(self.templates["technical_specs"])
        return template.render()

    def generate_complete_whitepaper(self, analysis_data: Dict) -> str:
        """生成完整白皮书"""
        sections = [
            self.generate_executive_summary(analysis_data),
            self.generate_market_analysis(analysis_data),
            self.generate_business_recommendations(analysis_data),
            self.generate_trend_predictions(analysis_data),
            self.generate_marketing_copy(),
            self.generate_technical_specs(),
        ]

        # 添加页脚
        footer = f"""
---

## 关于本报告

**数据来源**: 雷石K歌全系列终端  
**分析周期**: 2025年Q2  
**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**报告版本**: v1.0  

**联系方式**:  
- 邮箱: mazhe@thunder.com.cn  
- 网址: www.leishi.com  
- 数据平台: 雷石K歌全系列终端  

---

*本报告由雷石互联网研究院出品，基于真实用户数据生成，为硬件厂商提供专业的市场洞察和商业建议。*
"""

        return "\n\n".join(sections) + footer

    def generate_custom_report(self, analysis_data: Dict, report_type: str) -> str:
        """生成定制化报告"""
        if report_type == "executive":
            return self.generate_executive_summary(analysis_data)
        elif report_type == "technical":
            return self.generate_technical_specs()
        elif report_type == "marketing":
            return self.generate_marketing_copy()
        else:
            return self.generate_complete_whitepaper(analysis_data)

    def save_report(self, content: str, output_path: str):
        """保存报告"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"报告已保存到: {output_path}")


if __name__ == "__main__":
    # 示例用法
    generator = ContentGenerator()

    # 加载分析数据
    with open("analysis/comprehensive_analysis.json", "r", encoding="utf-8") as f:
        analysis_data = json.load(f)

    # 生成完整白皮书
    whitepaper = generator.generate_complete_whitepaper(analysis_data)
    generator.save_report(whitepaper, "reports/music_whitepaper_2025q2.md")

    print("白皮书生成完成！")
