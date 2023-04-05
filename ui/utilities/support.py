"""Supportive functions"""
import string

import allure
import yaml
import random
from sqlalchemy import create_engine, text
from ui.testdata.support_data import first_names, last_names, domains


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


@allure.step('Generate user data for sign up')
def user_data_generator(pass_length=9):
    user_data = []
    first_name = random.choice(first_names)
    user_data.append(first_name)
    last_name = random.choice(last_names)
    user_data.append(last_name)
    domain = random.choice(domains)
    email = f'{first_name.lower()}_{last_name.lower()}@{domain}'  # Workaround for email Uppercase
    user_data.append(email)
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(pass_length))
    user_data.append(password)
    return user_data
