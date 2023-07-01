from get_item_code import RakutenIchibaAPI
from conn_db import MySQL
from datetime import datetime
import time
import json

# 1.get item code list from db
# 2.access api by use item code

def lambda_handler():
    timestamp = str(time.time())
    json_file = open(timestamp +'.json', 'a')
    api = RakutenIchibaAPI()
    db = MySQL('zag_shop')
    items_db = db.get_item_from_table('zag_product_control')

    modify = []
    for item_db in items_db:
        item_api = api.search_product_by_item_code(item_db[5])
        # if not item_api:
        #     if item_db[7] == 1:
        #         i = {
        #             'item_code': item_db[5],
        #             'in_stock': 0,
        #             'price': 0,
        #         }
        #         modify.append(i)
        #     else:
        #         pass

        # else:
        #     if item_api.get('availability') != item_db[7]:
        #         i = {
        #             'item_code': item_db[5],
        #             'in_stock': item_api.get('availability'),
        #             'price': item_api.get('price'),
        #         }
        #         modify.append(i)
        #     else:
        #         pass
        # i = f"('item_code':{item_db[5]}, 'in_stock': {item_api.get('availability')}, 'price': {item_api.get('price')})"
        current_time = datetime.now()
        if item_api:
            i = {
                'product_id': item_db[1],
                'is_available': item_api.get('availability'),
                'price': item_api.get('itemPrice'),
                'is_take_off': not item_api.get('availability'),
                'take_off_time': str(current_time),
                'update_time': str(current_time),
                }
        else:
            i = {
                'product_id': item_db[1],
                'is_available': 0,
                'price': 0,
                'is_take_off': 1,
                'take_off_time': str(current_time),
                'update_time': str(current_time),
                }
        modify.append(i)
        # every 0.5 seconds make a request to rakuten api
        time.sleep(0.3)

    json_file.write(json.dumps(modify))
    json_file.close()
    db.backup_product_inventory()
    insert_into_db(timestamp +'.json')

def insert_into_db(filename):
    file = open(filename, "r")
    json_data = json.load(file)
    data = []
    for item in json_data:
        data.append((item['product_id'], item['is_available'], item['price'], item['is_take_off'], item['take_off_time'], item['update_time']))

    print(f'{len(data)} recodes will be inserted zag_shop.zag_product_inventory_history')
    zagShop = MySQL('zag_shop')
    zagShop.insert_into_product_inventory(data)

lambda_handler()