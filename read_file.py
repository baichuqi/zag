import json
from conn_db import MySQL

# 指定文件路径
file_path = "1686667701.3456936.json"
file = open(file_path, "r")
json_data = json.load(file)
data = []
for item in json_data:
    data.append((item['item_code'], item['in_stock'], item['price']))

print(len(data))
rakutencon = MySQL('rakutencon')
rakutencon.insert_into_product_inventory(data)
