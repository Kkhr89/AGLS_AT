"""Supportive functions"""

import allure
import yaml
from sqlalchemy import create_engine, text


@allure.step('Take key-related text')
def yaml_parser(file_name: str, key: str):
    with open(file_name, 'r') as f:
        exp_text = yaml.safe_load(f)[f'{key}']
    return exp_text


@allure.step('Connect to the database and execute SQL query')
def db_connect_execute_query_return_cell(host_link: str, sql_query: str):
    engine = create_engine(host_link)
    connection = engine.connect()
    result = connection.execute(text(sql_query))
    connection.close()
    return result.fetchone()[0]
