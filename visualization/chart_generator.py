#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音乐行业数据可视化模块
用于生成图表和仪表板
"""

import json
import os
from typing import Any, Dict, List

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False


class ChartGenerator:
    """图表生成器"""

    def __init__(self):
        self.output_dir = "visualization/charts"
        os.makedirs(self.output_dir, exist_ok=True)

    def create_top_songs_chart(self, songs_data: List[Dict]) -> str:
        """创建热门歌曲排行榜图表"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

        # 提取数据
        songs = [song["song_name"] for song in songs_data]
        playback_rates = [
            float(song["playback_rate"].rstrip("%")) for song in songs_data
        ]
        artists = [song["artist"] for song in songs_data]

        # 柱状图
        bars = ax1.barh(songs, playback_rates, color="skyblue", alpha=0.7)
        ax1.set_xlabel("点播占比 (%)")
        ax1.set_title("热门歌曲排行榜 TOP10", fontsize=16, fontweight="bold")
        ax1.grid(True, alpha=0.3)

        # 添加数值标签
        for i, (bar, rate) in enumerate(zip(bars, playback_rates)):
            ax1.text(
                rate + 0.05,
                bar.get_y() + bar.get_height() / 2,
                f"{rate}%",
                va="center",
                fontsize=10,
            )

        # 歌手分布饼图
        artist_counts = pd.Series(artists).value_counts()
        colors = plt.cm.Set3(np.linspace(0, 1, len(artist_counts)))

        wedges, texts, autotexts = ax2.pie(
            artist_counts.values,
            labels=artist_counts.index,
            autopct="%1.1f%%",
            colors=colors,
        )
        ax2.set_title("歌手分布", fontsize=14, fontweight="bold")

        plt.tight_layout()
        output_path = f"{self.output_dir}/top_songs_chart.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_user_demographics_chart(self, demographics: Dict) -> str:
        """创建用户画像图表"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

        # 性别分布
        gender_data = demographics["gender"]
        ax1.pie(
            gender_data.values(),
            labels=gender_data.keys(),
            autopct="%1.1f%%",
            colors=["lightblue", "lightpink"],
        )
        ax1.set_title("性别分布", fontsize=14, fontweight="bold")

        # 年龄分布
        age_data = demographics["age_groups"]
        age_groups = list(age_data.keys())
        age_values = list(age_data.values())

        bars = ax2.bar(age_groups, age_values, color="lightgreen", alpha=0.7)
        ax2.set_title("年龄分布", fontsize=14, fontweight="bold")
        ax2.set_ylabel("占比 (%)")

        # 添加数值标签
        for bar, value in zip(bars, age_values):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                f"{value}%",
                ha="center",
                va="bottom",
            )

        # 用户类型分布
        user_types = demographics["user_types"]
        user_names = list(user_types.keys())
        user_values = list(user_types.values())

        bars = ax3.barh(user_names, user_values, color="lightcoral", alpha=0.7)
        ax3.set_title("用户类型分布", fontsize=14, fontweight="bold")
        ax3.set_xlabel("占比 (%)")

        # 添加数值标签
        for bar, value in zip(bars, user_values):
            ax3.text(
                value + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"{value}%",
                va="center",
            )

        # 情绪标签分布（模拟数据）
        emotions = ["怀旧", "emo", "深情", "伤感", "青春", "励志"]
        emotion_values = [25, 20, 15, 15, 12, 13]

        bars = ax4.bar(emotions, emotion_values, color="gold", alpha=0.7)
        ax4.set_title("情绪标签分布", fontsize=14, fontweight="bold")
        ax4.set_ylabel("占比 (%)")
        ax4.tick_params(axis="x", rotation=45)

        # 添加数值标签
        for bar, value in zip(bars, emotion_values):
            ax4.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                f"{value}%",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        output_path = f"{self.output_dir}/user_demographics_chart.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_regional_trends_chart(self, regional_data: List[Dict]) -> str:
        """创建地域偏好趋势图表"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

        # 市场占有率
        city_types = [region["city_type"] for region in regional_data]
        market_shares = [region["market_share"] for region in regional_data]

        bars = ax1.bar(city_types, market_shares, color="lightsteelblue", alpha=0.7)
        ax1.set_title("各城市等级市场占有率", fontsize=14, fontweight="bold")
        ax1.set_ylabel("市场占有率 (%)")
        ax1.tick_params(axis="x", rotation=45)

        # 添加数值标签
        for bar, share in zip(bars, market_shares):
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                f"{share}%",
                ha="center",
                va="bottom",
            )

        # 标签偏好热力图（模拟数据）
        tags = ["怀旧", "emo", "对唱", "演唱会", "港风", "翻红"]
        city_types_short = ["一线", "新一线", "二线", "三线"]

        # 模拟偏好矩阵
        preference_matrix = np.array(
            [
                [0.8, 0.3, 0.2, 0.9, 0.1, 0.4],
                [0.4, 0.9, 0.7, 0.3, 0.2, 0.8],
                [0.2, 0.5, 0.9, 0.4, 0.8, 0.6],
                [0.1, 0.2, 0.3, 0.1, 0.4, 0.9],
            ]
        )

        im = ax2.imshow(preference_matrix, cmap="YlOrRd", aspect="auto")
        ax2.set_xticks(range(len(tags)))
        ax2.set_yticks(range(len(city_types_short)))
        ax2.set_xticklabels(tags, rotation=45)
        ax2.set_yticklabels(city_types_short)
        ax2.set_title("地域标签偏好热力图", fontsize=14, fontweight="bold")

        # 添加颜色条
        plt.colorbar(im, ax=ax2, label="偏好强度")

        plt.tight_layout()
        output_path = f"{self.output_dir}/regional_trends_chart.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_time_patterns_chart(self, time_data: Dict) -> str:
        """创建时间使用模式图表"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

        # 24小时使用曲线
        hours = list(range(24))
        # 模拟使用率数据
        usage_rates = [
            0.05,
            0.03,
            0.02,
            0.01,
            0.01,
            0.02,
            0.05,
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85,
            0.90,
            0.85,
            0.75,
            0.65,
            0.55,
            0.45,
            0.35,
            0.25,
            0.15,
        ]

        ax1.plot(hours, usage_rates, "b-", linewidth=2, marker="o")
        ax1.fill_between(hours, usage_rates, alpha=0.3, color="skyblue")
        ax1.set_xlabel("时间 (小时)")
        ax1.set_ylabel("使用率")
        ax1.set_title("24小时使用模式", fontsize=14, fontweight="bold")
        ax1.grid(True, alpha=0.3)
        ax1.set_xticks(range(0, 24, 2))

        # 设备使用时长对比
        devices = list(time_data["device_usage"].keys())
        durations = []
        device_names = []

        for device, info in time_data["device_usage"].items():
            duration_str = info["avg_duration"]
            # 简单解析时长（实际应用中需要更复杂的解析）
            if "h" in duration_str:
                hours = int(duration_str.split("h")[0])
                minutes = (
                    int(duration_str.split("h")[1].split("m")[0])
                    if "m" in duration_str.split("h")[1]
                    else 0
                )
                total_minutes = hours * 60 + minutes
            else:
                total_minutes = int(duration_str.split("m")[0])

            durations.append(total_minutes)
            device_names.append(device.replace("_", " ").title())

        bars = ax2.bar(device_names, durations, color="lightgreen", alpha=0.7)
        ax2.set_title("设备平均使用时长", fontsize=14, fontweight="bold")
        ax2.set_ylabel("时长 (分钟)")
        ax2.tick_params(axis="x", rotation=45)

        # 添加数值标签
        for bar, duration in zip(bars, durations):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 2,
                f"{duration}分钟",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        output_path = f"{self.output_dir}/time_patterns_chart.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_tag_trends_chart(self, tag_data: List[Dict]) -> str:
        """创建标签趋势图表"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

        # 标签频率柱状图
        tags = [tag["tag"] for tag in tag_data]
        frequencies = [tag["frequency"] for tag in tag_data]

        bars = ax1.bar(tags, frequencies, color="lightcoral", alpha=0.7)
        ax1.set_title("标签出现频率", fontsize=14, fontweight="bold")
        ax1.set_ylabel("出现次数")
        ax1.tick_params(axis="x", rotation=45)

        # 添加数值标签
        for bar, freq in zip(bars, frequencies):
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 100,
                f"{freq:,}",
                ha="center",
                va="bottom",
            )

        # 增长率对比
        growth_rates = [tag["growth_rate"] for tag in tag_data]
        predicted_growth = [tag["predicted_growth"] for tag in tag_data]

        x = np.arange(len(tags))
        width = 0.35

        bars1 = ax2.bar(
            x - width / 2,
            growth_rates,
            width,
            label="当前增长率",
            color="lightblue",
            alpha=0.7,
        )
        bars2 = ax2.bar(
            x + width / 2,
            predicted_growth,
            width,
            label="预测增长率",
            color="lightgreen",
            alpha=0.7,
        )

        ax2.set_title("标签增长率对比", fontsize=14, fontweight="bold")
        ax2.set_ylabel("增长率 (%)")
        ax2.set_xticks(x)
        ax2.set_xticklabels(tags, rotation=45)
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # 添加数值标签
        for bar, rate in zip(bars1, growth_rates):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                f"{rate}%",
                ha="center",
                va="bottom",
            )

        for bar, rate in zip(bars2, predicted_growth):
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.5,
                f"{rate}%",
                ha="center",
                va="bottom",
            )

        plt.tight_layout()
        output_path = f"{self.output_dir}/tag_trends_chart.png"
        plt.savefig(output_path, dpi=300, bbox_inches="tight")
        plt.close()

        return output_path

    def create_dashboard(self, analysis_data: Dict) -> str:
        """创建综合仪表板"""
        # 这里可以创建一个包含多个子图的综合仪表板
        # 为了简化，我们创建一个包含所有图表的HTML报告

        dashboard_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>音乐行业数据仪表板</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .chart-container { margin: 20px 0; }
                .chart-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; }
                img { max-width: 100%; height: auto; }
            </style>
        </head>
        <body>
            <h1>音乐行业数据仪表板</h1>
            <p>基于雷石K歌全系列终端数据分析</p>
            
            <div class="chart-container">
                <div class="chart-title">热门歌曲排行榜</div>
                <img src="charts/top_songs_chart.png" alt="热门歌曲排行榜">
            </div>
            
            <div class="chart-container">
                <div class="chart-title">用户画像分析</div>
                <img src="charts/user_demographics_chart.png" alt="用户画像分析">
            </div>
            
            <div class="chart-container">
                <div class="chart-title">地域偏好趋势</div>
                <img src="charts/regional_trends_chart.png" alt="地域偏好趋势">
            </div>
            
            <div class="chart-container">
                <div class="chart-title">时间使用模式</div>
                <img src="charts/time_patterns_chart.png" alt="时间使用模式">
            </div>
            
            <div class="chart-container">
                <div class="chart-title">标签趋势分析</div>
                <img src="charts/tag_trends_chart.png" alt="标签趋势分析">
            </div>
        </body>
        </html>
        """

        output_path = f"{self.output_dir}/dashboard.html"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(dashboard_html)

        return output_path

    def generate_all_charts(self, analysis_data: Dict) -> Dict[str, str]:
        """生成所有图表"""
        chart_paths = {}

        # 模拟数据用于图表生成
        songs_data = [
            {
                "song_name": "漂洋过海来看你",
                "artist": "李宗盛",
                "playback_rate": "2.9%",
            },
            {"song_name": "想你的夜", "artist": "关喆", "playback_rate": "2.7%"},
            {"song_name": "那女孩对我说", "artist": "黄义达", "playback_rate": "2.6%"},
            {"song_name": "后来", "artist": "刘若英", "playback_rate": "2.4%"},
            {"song_name": "演员", "artist": "薛之谦", "playback_rate": "2.3%"},
            {
                "song_name": "你就不要想起我",
                "artist": "田馥甄",
                "playback_rate": "2.2%",
            },
            {"song_name": "一路向北", "artist": "周杰伦", "playback_rate": "2.1%"},
            {"song_name": "平凡之路", "artist": "朴树", "playback_rate": "2.0%"},
            {"song_name": "起风了", "artist": "买辣椒也用券", "playback_rate": "1.9%"},
            {"song_name": "说好的幸福呢", "artist": "周杰伦", "playback_rate": "1.8%"},
        ]

        # 生成各种图表
        chart_paths["top_songs"] = self.create_top_songs_chart(songs_data)
        chart_paths["user_demographics"] = self.create_user_demographics_chart(
            analysis_data["detailed_analysis"]["user_demographics"]
        )
        chart_paths["regional_trends"] = self.create_regional_trends_chart(
            analysis_data["detailed_analysis"]["regional_trends"]
        )
        chart_paths["time_patterns"] = self.create_time_patterns_chart(
            analysis_data["detailed_analysis"]["time_patterns"]
        )
        chart_paths["tag_trends"] = self.create_tag_trends_chart(
            analysis_data["detailed_analysis"]["tag_trends"]
        )
        chart_paths["dashboard"] = self.create_dashboard(analysis_data)

        return chart_paths


if __name__ == "__main__":
    # 示例用法
    generator = ChartGenerator()

    # 加载分析数据
    with open("analysis/comprehensive_analysis.json", "r", encoding="utf-8") as f:
        analysis_data = json.load(f)

    # 生成所有图表
    chart_paths = generator.generate_all_charts(analysis_data)

    print("图表生成完成！")
    for chart_name, path in chart_paths.items():
        print(f"{chart_name}: {path}")
