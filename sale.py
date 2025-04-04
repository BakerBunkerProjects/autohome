import requests
import pandas as pd
import json
from datetime import datetime

# 获取当前时间
now = datetime.now()
# 计算上个月（注意跨年情况）
if now.month == 1:
    last_month = now.replace(year=now.year - 1, month=12)
else:
    last_month = now.replace(month=now.month - 1)
# 格式化为 "YYYYMM"
last_month_str = last_month.strftime("%Y%m")
print(last_month_str)
data = requests.get(
    f"https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&count=100000&rank_data_type=11&nation=0&month={last_month_str}"
)

datas = json.loads(data.text)["data"]["list"]

data_list = []

for item in datas:
    data_list.append(
        {
            "brand_name": item["brand_name"],
            "sub_brand_name": item["sub_brand_name"],
            "series_name": item["series_name"],
            "sales": item["count"],
        }
    )
    # print(f"{item['brand_name']}-{item['sub_brand_name']}-{item['series_name']}")
    # print(item["count"])

pd.DataFrame(data_list).to_csv(f"./sale-{last_month_str}.csv")
