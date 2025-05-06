# JSON, YAML, TOML
import json
import yaml

from dataclasses import dataclass
from typing import Callable

@dataclass
class SomeItem:
    item_id: int
    owner_id: int
    name: str
    description: str
    price: int
    action: Callable


def default_action(item: SomeItem):
    print(item.name, item.price)


item = SomeItem(
    3867657643, 
    43571564, 
    'Настольная лампа', 
    'Cozy light many modes made in China desk lamp', 
    10000,
    default_action,
)
with open('item.json', 'w', encoding='utf-8') as fd:
    json.dump(item.__dict__, fd, indent=2, sort_keys=True, ensure_ascii=False, default=str)
    
# json.dump(примитивное значение | массив примитивов | словарь[str, примитивы] | массив_или_словарь[других таких же объектов])

# Представим, что ниже код другого сервиса

with open('item.json', encoding='utf-8') as fd:
    json_item = json.load(fd)
    new_item = SomeItem(**json_item)

print(new_item.name, new_item.price)

with open('config.yaml') as fd:
    config = yaml.load(fd, yaml.FullLoader)
with open('config.json', 'w') as fd:
    json.dump(config, fd, indent=2)
    
# pickle / dill

import pickle
import dill

item = SomeItem(
    3867657643, 
    43571564, 
    'Настольная лампа', 
    'Cozy light many modes made in China desk lamp', 
    10000,
    default_action,
)
with open('item.binary2', 'wb') as fd:
    dill.dump(item, fd)

with open('item.binary2', 'rb') as fd:
    new_item = dill.load(fd, encoding='utf-8')

print(type(new_item))
new_item.action(new_item)