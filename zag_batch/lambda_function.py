import json
import boto3
import time
from get_items_qaulity import MySQL

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('lambda')
    db = MySQL('zag_shop')
    quality_db = db.get_item_from_table('zag_product_control')
    
    quality = quality_db[0][0] if quality_db else 0
    
    invoke_list = []
    if quality:
        print(quality)
        num = 1500
        index = int(quality/num)
        for i in range(0, index + 1):
            obj = (i * num, num)
            invoke_list.append(obj)
            
    for lambda_in in invoke_list:
        # print(lambda_in[0], lambda_in[1])

        response = client.invoke(
            FunctionName='arn:aws:lambda:ap-northeast-1:225873644162:function:product_inventory',
            InvocationType='Event',  # 使用Event类型异步触发Lambda函数
            Payload=json.dumps(lambda_in)  # 传递的触发载荷
        )
        time.sleep(10)

    return {
        'statusCode': 200,
        'body': len(invoke_list)
    }
