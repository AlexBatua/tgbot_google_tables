import json

config_path = 'config.json'


def get_tg_token() -> str:
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config['tg_token']
