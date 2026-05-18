import os
import json
import random

# 配置区域
MOCK_MODE = True  # 开启 Mock 测试模式

def get_bemob_stats_mock():
    """生成 Mock 数据以验证监控逻辑"""
    print("--- [MOCK MODE] 生成测试数据 ---")
    return [
        {
            "campaign_id": "285cb144-8f56-4387-a220-7cdc57b041bb",
            "name": "Profitable Campaign",
            "cost": 100.0,
            "revenue": 150.0  # ROI: 50%
        },
        {
            "campaign_id": "648f7a06-a443-4514-875f-16b48f70da91",
            "name": "Lossy Campaign",
            "cost": 100.0,
            "revenue": 60.0   # ROI: -40% (应触发报警)
        }
    ]

def update_hilltop_bid_mock(campaign_id, new_bid):
    """模拟 HilltopAds 降价操作"""
    print(f"[MOCK] 成功: Campaign {campaign_id} 出价调整为 {new_bid}")
    return True

def log_alert(message):
    """记录报警到 alert.log"""
    with open("alert.log", "a") as f:
        f.write(message + "\n")
    print(f"!!! [报警记录] {message}")

def monitor():
    stats = get_bemob_stats_mock()
    
    for row in stats:
        c_id = row['campaign_id']
        cost = row['cost']
        rev = row['revenue']
        roi = (rev - cost) / cost if cost > 0 else 0
        
        print(f"Campaign: {row['name']} ({c_id}) | ROI: {roi:.2%}")
        
        if roi < -0.20:
            msg = f"检测到亏损 Campaign: {c_id}, ROI: {roi:.2%}"
            log_alert(msg)
            # 降价逻辑
            if update_hilltop_bid_mock(c_id, 0.9):
                print("--> 自动执行降价策略")
        else:
            print("--> ROI 正常")

if __name__ == "__main__":
    monitor()
