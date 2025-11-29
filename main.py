import requests
import json
from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

def get_weather(city, api_key):
    """
    调用天气API获取城市天气信息
    :param city: 城市名称
    :param api_key: API密钥
    :return: 天气信息字典
    """
    url = "https://v2.xxapi.cn/api/weatherDetails"
    params = {
        "key": api_key,
        "city": city
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        
        data = response.json()
        
        # 检查API返回状态
        if data.get("code") != 0:
            raise Exception(f"API请求失败: {data.get('msg', '未知错误')}")
        
        return data.get("data", {})
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"网络请求错误: {str(e)}")
    except json.JSONDecodeError:
        raise Exception("API返回数据格式错误")
    except Exception as e:
        raise e

def main():
    print("=== 天气查询工具 ===")
    print()
    
    # 从环境变量获取API Key
    api_key = os.getenv("key")
    if not api_key:
        print("错误：未找到API Key，请检查.env文件")
        return
    
    # 请用户输入城市名称
    city = input("请输入要查询的城市：")
    if not city:
        print("错误：城市名称不能为空")
        return
    
    try:
        print(f"\n正在查询{city}的天气信息...")
        weather_data = get_weather(city, api_key)
        
        if not weather_data:
            print("未获取到天气信息")
            return
        
        # 展示天气信息（根据实际API返回字段调整）
        print(f"\n=== {city}天气信息 ===")
        print(f"日期：{weather_data.get('date', '未知')}")
        print(f"时间：{weather_data.get('time', '未知')}")
        print(f"天气：{weather_data.get('weather', '未知')}")
        print(f"温度：{weather_data.get('temperature', '未知')}°C")
        print(f"湿度：{weather_data.get('humidity', '未知')}%")
        print(f"风向：{weather_data.get('wind_direction', '未知')}")
        print(f"风力：{weather_data.get('wind_power', '未知')}")
        print(f"空气质量：{weather_data.get('air_quality', '未知')}")
        print(f"PM2.5：{weather_data.get('pm25', '未知')}")
        
    except Exception as e:
        print(f"查询失败：{str(e)}")

if __name__ == "__main__":
    main()
