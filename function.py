from get_item_code import RakutenIchibaAPI
from conn_db import MySQL
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
        if item_api: 
            i = {'item_code': item_db[5],'in_stock': item_api.get('availability'),'price': item_api.get('itemPrice')}
            modify.append(i)
        # every 0.5 seconds make a request to rakuten api
        time.sleep(0.5)

    json_file.write(json.dumps(modify))
    json_file.close()
    insert_into_db(timestamp +'.json')

def insert_into_db(filename):
    file = open(filename, "r")
    json_data = json.load(file)
    data = []
    for item in json_data:
        data.append((item['item_code'], item['in_stock'], item['price']))

    print(f'{len(data)} recodes will be inserted rakutencon.zag_product_inventory_history')
    rakutencon = MySQL('rakutencon')
    rakutencon.insert_into_product_inventory(data)

lambda_handler()