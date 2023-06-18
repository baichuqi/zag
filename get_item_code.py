import requests
import time
import json


class RakutenIchibaAPI():
    def __init__(self) -> None:
        self.api_key = '1022685646904592420'
        self.base_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'

    def search_product_by_item_code(self, item_code):
        params = {
            'format': 'json',
            'itemCode': item_code,
            'elements': 'itemCode,itemPrice,availability',
            'applicationId': self.api_key
        }
        result = self.__get_response(params)
        # print(len(result.get('Items'))>0)
        item = None
        if not result:
            return item

        if len(result.get('Items')) > 0:
            item = result.get('Items')[0].get('Item', None)

        return item

    def search_product_by_shopCode(self, shopCode, page):
        params = {
            'format': 'json',
            'shopCode': shopCode,
            'elements': 'itemCode,itemPrice,availability',
            'hits': 30,
            'page': page,
            'applicationId': self.api_key
        }
        result = self.__get_response(params)
        return result

    def search_pd_count_page(self, shopCode):
        params = {
            'format': 'json',
            'shopCode': shopCode,
            'elements': 'pageCount',
            'applicationId': self.api_key
        }
        pageCount = self.__get_response(params)
        return pageCount.get('pageCount', 0)

    def write_in_json_file(self):
        timestamp = str(time.time())
        json_file = open(timestamp +'.json', 'a')
        # pageCounts = self.search_pd_count_page('murasaki-sports')
        pageCounts = 2
        page = 1
        while page < pageCounts + 1:
            data = self.search_product_by_shopCode('murasaki-sports', page)
            json_file.write(json.dumps(data) + '\n')
            page += 1
            time.sleep(10)
        json_file.close()

    def __get_response(self, params):

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            print(response.status_code)
            print(response)

        else:
            return response.json()

# api = RakutenIchibaAPI()
# item = api.search_product_by_item_code('victoria-online:18683888')
# print(api.search_pd_count_page("murasaki-sports"))

# api.write_in_json_file()

