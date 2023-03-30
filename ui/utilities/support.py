"""Supportive functions"""

import yaml


def yaml_parser(file_name: str, key: str):
    with open(file_name, 'r') as f:
        exp_text = yaml.safe_load(f)[f'{key}']
    return exp_text
