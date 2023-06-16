import json
import time
import boto3
from rakutenApi import RakutenIchibaAPI
from conn_db import MySQL

def lambda_handler(event, context):
    # TODO implement
    timestamp = str(time.time())
    print("create json file to save data.")
    json_file = open('/tmp/' + timestamp +'.json', 'a')
    
    api = RakutenIchibaAPI()
    db = MySQL('zag_shop')
    items_db = db.get_item_from_table('zag_product_control', event[0], event[1])
    
    modify = []
    print("fetch data from rakuten API.")
    for item_db in items_db:
        item_api = api.search_product_by_item_code(item_db[5])
        if item_api: 
            i = {'item_code': item_db[5],'in_stock': item_api.get('availability'),'price': item_api.get('itemPrice')}
            modify.append(i)
        time.sleep(0.5)

    print("save the data into json file." + timestamp +".json")
    json_file.write(json.dumps(modify))
    json_file.close()
    
    print("insert data into database.")
    insert_into_db('/tmp/' + timestamp +'.json')

    s3 = boto3.resource('s3')
    s3.Bucket('zag-log').upload_file('/tmp/' + timestamp +'.json', 'zag-log' + timestamp +'.json')

    return {
        'statusCode': 200,
        'body': 'send '+timestamp +'.json to s3://zag-log'
    }

def insert_into_db(filename):
    file = open(filename, "r")
    json_data = json.load(file)
    data = []
    for item in json_data:
        data.append((item['item_code'], item['in_stock'], item['price']))

    print(f'{len(data)} recodes will be inserted rakutencon.zag_product_inventory_history')
    rakutencon = MySQL('rakutencon')
    rakutencon.insert_into_product_inventory(data)