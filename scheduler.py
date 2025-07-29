#!/usr/bin/env python3
"""
音乐白皮书自动化生成调度器
支持每周、每月、每季度自动生成白皮书
"""

import os
import sys
import json
import schedule
import time
from datetime import datetime, timedelta
import subprocess
import logging
from pathlib import Path

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scheduler.log'),
        logging.StreamHandler()
    ]
)

class WhitepaperScheduler:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.reports_dir = self.project_root / "reports"
        self.data_dir = self.project_root / "data"
        
    def generate_weekly_report(self):
        """生成周报"""
        try:
            logging.info("开始生成周报...")
            current_date = datetime.now()
            week_start = current_date - timedelta(days=current_date.weekday())
            week_end = week_start + timedelta(days=6)
            
            report_name = f"weekly_report_{week_start.strftime('%Y%m%d')}_{week_end.strftime('%Y%m%d')}.md"
            report_path = self.reports_dir / report_name
            
            # 运行主程序生成报告
            result = subprocess.run([sys.executable, "main.py", "--period", "weekly"], 
                                  capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                logging.info(f"周报生成成功: {report_name}")
                self.commit_to_git(f"Add weekly report: {report_name}")
            else:
                logging.error(f"周报生成失败: {result.stderr}")
                
        except Exception as e:
            logging.error(f"生成周报时出错: {str(e)}")
    
    def generate_monthly_report(self):
        """生成月报"""
        try:
            logging.info("开始生成月报...")
            current_date = datetime.now()
            month_start = current_date.replace(day=1)
            next_month = (month_start + timedelta(days=32)).replace(day=1)
            month_end = next_month - timedelta(days=1)
            
            report_name = f"monthly_report_{month_start.strftime('%Y%m')}.md"
            report_path = self.reports_dir / report_name
            
            # 运行主程序生成报告
            result = subprocess.run([sys.executable, "main.py", "--period", "monthly"], 
                                  capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                logging.info(f"月报生成成功: {report_name}")
                self.commit_to_git(f"Add monthly report: {report_name}")
            else:
                logging.error(f"月报生成失败: {result.stderr}")
                
        except Exception as e:
            logging.error(f"生成月报时出错: {str(e)}")
    
    def generate_quarterly_report(self):
        """生成季报"""
        try:
            logging.info("开始生成季报...")
            current_date = datetime.now()
            quarter = (current_date.month - 1) // 3 + 1
            year = current_date.year
            
            quarter_start_month = (quarter - 1) * 3 + 1
            quarter_start = current_date.replace(month=quarter_start_month, day=1)
            
            if quarter == 4:
                quarter_end = current_date.replace(year=year+1, month=1, day=1) - timedelta(days=1)
            else:
                quarter_end = current_date.replace(month=quarter_start_month+3, day=1) - timedelta(days=1)
            
            report_name = f"quarterly_report_{year}Q{quarter}.md"
            report_path = self.reports_dir / report_name
            
            # 运行主程序生成报告
            result = subprocess.run([sys.executable, "main.py", "--period", "quarterly"], 
                                  capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                logging.info(f"季报生成成功: {report_name}")
                self.commit_to_git(f"Add quarterly report: {report_name}")
            else:
                logging.error(f"季报生成失败: {result.stderr}")
                
        except Exception as e:
            logging.error(f"生成季报时出错: {str(e)}")
    
    def commit_to_git(self, message):
        """提交到Git"""
        try:
            subprocess.run(["git", "add", "."], cwd=self.project_root, check=True)
            subprocess.run(["git", "commit", "-m", message], cwd=self.project_root, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=self.project_root, check=True)
            logging.info(f"Git提交成功: {message}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Git操作失败: {str(e)}")
    
    def setup_schedule(self):
        """设置调度任务"""
        # 每周一上午9点生成周报
        schedule.every().monday.at("09:00").do(self.generate_weekly_report)
        
        # 每月1号上午10点生成月报
        schedule.every().day.at("10:00").do(self.check_monthly_report)
        
        # 每季度第一天上午11点生成季报
        schedule.every().day.at("11:00").do(self.check_quarterly_report)
        
        logging.info("调度任务已设置完成")
    
    def check_monthly_report(self):
        """检查是否需要生成月报"""
        if datetime.now().day == 1:
            self.generate_monthly_report()
    
    def check_quarterly_report(self):
        """检查是否需要生成季报"""
        current_date = datetime.now()
        if current_date.day == 1 and current_date.month in [1, 4, 7, 10]:
            self.generate_quarterly_report()
    
    def run(self):
        """运行调度器"""
        logging.info("启动音乐白皮书调度器...")
        self.setup_schedule()
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次

def main():
    scheduler = WhitepaperScheduler()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "weekly":
            scheduler.generate_weekly_report()
        elif command == "monthly":
            scheduler.generate_monthly_report()
        elif command == "quarterly":
            scheduler.generate_quarterly_report()
        elif command == "run":
            scheduler.run()
        else:
            print("用法: python scheduler.py [weekly|monthly|quarterly|run]")
    else:
        scheduler.run()

if __name__ == "__main__":
    main() 