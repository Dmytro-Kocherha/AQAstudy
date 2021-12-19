import json


class JsonDataGetter:
    with open("config_data.json", encoding='utf-8') as config_data:
        data = json.load(config_data)
    browser_name = data['browser_name']
    url = data['url']

