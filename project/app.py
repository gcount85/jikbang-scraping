import pandas as pd
import requests
import json

df = pd.DataFrame()

# 23/3/31 5:13PM 36072451번이 최신
to_num = 36072451
how_many = 10000
from_num = to_num - how_many


for i in range(from_num, to_num + 1):
    try:
        # req = requests.get("https://apis.zigbang.com/v2/store/article/stores/574037") # 상가 매물
        req = requests.get(
            f"https://apis.zigbang.com/v2/items/{i}")  # 거주 목적 매물
        data = json.loads(req.text)

        item = data['item']
        agent = data['agent']

        # Convert JSON data to pandas DataFrame
        df = pd.json_normalize(data)

        # Convert data DataFrame into Excel file
        df.to_excel('C:/Users/jamie/Documents/store_analysis.xlsx')
    except:
        pass
