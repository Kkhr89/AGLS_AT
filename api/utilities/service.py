import json
import allure

@allure.step('Parse data from json file')
def parse_json_file(file_path: str):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
